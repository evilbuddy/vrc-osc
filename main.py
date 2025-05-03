import argparse
import time
import importlib.util
from pythonosc import udp_client

modules = []

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
                        help="The IP of the OSC server")
    parser.add_argument("--port", type=int, default=9000,
                        help="The port the OSC server is listening on")
    parser.add_argument("--sleep", type=int, default=1500,
                        help="The time between each update")
    parser.add_argument("--path", default="/chatbox/input",
                        help="The path to send the messages to")
    args = parser.parse_args()

    with open("modules.txt", "r") as f:
        for filename in f.readlines():
            filename = filename.strip()

            if filename[0] == "#":
                print(f'Module "{filename}" is commented, ignoring.')
                continue

            print(f'Importing module "{filename}"...')

            spec = importlib.util.spec_from_file_location(filename, "modules/" + filename + ".py")
            module = importlib.util.module_from_spec(spec)

            spec.loader.exec_module(module)

            if hasattr(module, "format"):
                print(f'Registering the "{filename}" module')
                modules.append(module)

                if hasattr(module, "init"):
                    print(f'The Module "{filename}" has an init function, running...')
                    module.init()
            else:
                print(f'The module "{filename}" does not have a format function, ignoring.')

    client = udp_client.SimpleUDPClient(args.ip, args.port)

    while(True):
        file = open("text.txt")
        text = file.read()
        file.close()

        for module in modules:
            text = module.format(text)
            time.sleep(args.sleep / 1000)

        client.send_message(args.path, [text, True])

