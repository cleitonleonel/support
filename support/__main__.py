from __future__ import absolute_import
from support.service import get_platform, resource_path, config,\
    ShareDesktop, ngrok


if __name__ == '__main__':
    arch_path = '64bits'
    if get_platform()[1] == 'armv7l':
        arch_path = 'arm'
    config.DEFAULT_NGROK_PATH = resource_path(f"bin/{arch_path}/ngrok")
    desktop = ShareDesktop()
    try:
        process = desktop.send_email()
        process.proc.wait()
    except KeyboardInterrupt:
        print("Shutting down server.")
        ngrok.kill()
        desktop.kill_threads()
