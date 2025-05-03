# hwinfo
#
# Dependencies:
#   psutil
#   GPUtil
# 
# Keys:
# {cpu_model}       Your CPU's name
# {cpu_pcores}      Your CPU's physical cores
# {cpu_cores}       Your CPU's total threads (threads * cores)
# {cpu_maxfreq}     Your CPU's maximum frequency
# {cpu_minfreq}     Your CPU's minimum frequency
# {cpu_curfreq}     Your CPU's current frequency
# {cpu_percent}       Your CPU's current usage
# 
# {gpu_model}       Your GPU's name
# {gpu_percent}     Your GPU's current usage
# {vram_total}      Your GPU's total VRAM
# {vram_free}       Your GPU's free VRAM
# {vram_used}       Your GPU's used VRAM
# {vram_percent}    Your GPU's current VRAM usage
#
# {ram_total}       Your total RAM
# {ram_available}   Your available RAM
# {ram_used}        Your used RAM
# {ram_free}        Your free RAM
# {ram_percent}     Your current RAM usage

import psutil
import platform
import GPUtil
import vrcosc

def cpu(text):
    return vrcosc.str_replace_bulk(text, {
        "cpu_model": platform.processor(),
        "cpu_pcores": psutil.cpu_count(logical=False),
        "cpu_cores": psutil.cpu_count(logical=True),
        "cpu_maxfreq": round(psutil.cpu_freq().max / 1000, 2),
        "cpu_minfreq": round(psutil.cpu_freq().min / 1000, 2), 
        "cpu_curfreq": round(psutil.cpu_freq().current / 1000, 2),
        "cpu_percent": psutil.cpu_percent()
    })

def gpu(text):
    gpu = GPUtil.getGPUs()[0]
    return vrcosc.str_replace_bulk(text, {
        "gpu_model": gpu.name,
        "gpu_percent": round(gpu.load * 100, 1),
        "vram_total": gpu.memoryTotal,
        "vram_free": gpu.memoryFree,
        "vram_used": gpu.memoryUsed,
        "vram_percent": gpu.memoryUsed / gpu.memoryTotal * 100 
    })

def ram(text):
    ram = psutil.virtual_memory()
    return vrcosc.str_replace_bulk(text, {
        "ram_total": round(ram.total / (1024 ** 3), 2),
        "ram_available": round(ram.available / (1024 ** 3), 2),
        "ram_used": round(ram.used / (1024 ** 3), 2),
        "ram_free": round(ram.free / (1024 ** 3), 2),
        "ram_percent": ram.percent

    })

def format(text):
    return cpu(gpu(ram(text)))
