from flask import current_app, request, send_from_directory
from webargs import fields
from webargs.flaskparser import use_args, FlaskParser
from random import seed

from . import main
from .config import firmware_path
from .firmware import MachineType, firmware_filename, firmware_upgrade_required, minimum_firmware
from .model import PicoStillSession
from .session_parser import active_still_sessions


arg_parser = FlaskParser()
seed(1)

events = {}


# Get Firmware: /firmware/picostill/<version>
#     Response: RAW Bin File
@main.route('/firmware/picostill/<file>', methods=['GET'])
def process_picostill_firmware(file):
    current_app.logger.debug('DEBUG: PicoStill fetch firmware file={}'.format(file))
    return send_from_directory(firmware_path(MachineType.PICOSTILL), file)


picostill_check_firmware_args = {
    'uid': fields.Str(required=True),       # 32 character alpha-numeric serial number
    'version': fields.Str(required=True),   # Current firmware version - i.e. 0.0.30
}


# Check Firmware: /API/PicoStill/getFirmwareAddress?uid={UID}&version={VERSION}
#       Response: '#{0}#' where {0} : {URL} = Url of firmware, -1 = No Updates
@main.route('/API/PicoStill/getFirmwareAddress', methods=['GET'])
@use_args(picostill_check_firmware_args, location='querystring')
def process_picostill_check_firmware(args):
    uid = args['uid']
    if uid not in active_still_sessions:
        active_still_sessions[uid] = PicoStillSession(uid)

    active_still_sessions[uid].ip_address = still_ip_address(request)

    if firmware_upgrade_required(MachineType.PICOSTILL, args['version']):
        filename = firmware_filename(MachineType.PICOSTILL, minimum_firmware(MachineType.PICOSTILL))
        return '#http://picobrew.com/firmware/picostill/{}#'.format(filename)
    return '#-1#'


# -------- Utility --------
def still_ip_address(request):
    headers_list = request.headers.getlist("X-Forwarded-For")
    ip_address = headers_list[0] if headers_list else request.remote_addr
    return ip_address
