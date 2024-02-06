import blackboxprotobuf
from datetime import *
from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, is_platform_windows, convert_utc_human_to_timezone, kmlgen, timeline

def get_googleLastTrip(files_found, report_folder, seeker, wrap_text, time_offset):
    data_list = []
    
    typess = {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'3': {'type': 'message', 'message_typedef': {'3': {'type': 'fixed64', 'name': ''}, '4': {'type': 'fixed64', 'name': ''}}, 'name': ''}, '5': {'type': 'int', 'name': ''}, '6': {'type': 'int', 'name': ''}, '1': {'type': 'bytes', 'name': ''}, '2': {'type': 'bytes', 'name': ''}}, 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'double', 'name': ''}, '2': {'type': 'fixed64', 'name': ''}, '3': {'type': 'fixed64', 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'fixed32', 'name': ''}, '2': {'type': 'fixed32', 'name': ''}, '3': {'type': 'fixed32', 'name': ''}}, 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}, '4': {'type': 'fixed32', 'name': ''}}, 'name': ''}, '6': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'5': {'type': 'int', 'name': ''}, '8': {'type': 'int', 'name': ''}, '9': {'type': 'int', 'name': ''}, '14': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '17': {'type': 'int', 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '5': {'type': 'message', 'message_typedef': {'6': {'type': 'int', 'name': ''}}, 'name': ''}, '8': {'type': 'int', 'name': ''}, '26': {'type': 'int', 'name': ''}, '27': {'type': 'message', 'message_typedef': {'2': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}, '4': {'type': 'int', 'name': ''}, '5': {'type': 'int', 'name': ''}, '6': {'type': 'int', 'name': ''}, '7': {'type': 'int', 'name': ''}}, 'name': ''}, '31': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}, '32': {'type': 'int', 'name': ''}, '34': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '45': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '4': {'type': 'int', 'name': ''}, '7': {'type': 'int', 'name': ''}, '8': {'type': 'int', 'name': ''}, '10': {'type': 'int', 'name': ''}, '16': {'type': 'int', 'name': ''}, '17': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}, '4': {'type': 'int', 'name': ''}, '5': {'type': 'int', 'name': ''}, '6': {'type': 'int', 'name': ''}, '7': {'type': 'int', 'name': ''}, '8': {'type': 'int', 'name': ''}, '10': {'type': 'int', 'name': ''}, '11': {'type': 'int', 'name': ''}}, 'name': ''}, '21': {'type': 'int', 'name': ''}, '22': {'type': 'int', 'name': ''}, '23': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}, '24': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}}, 'name': ''}, '25': {'type': 'int', 'name': ''}, '26': {'type': 'int', 'name': ''}, '27': {'type': 'int', 'name': ''}, '30': {'type': 'int', 'name': ''}, '32': {'type': 'int', 'name': ''}, '42': {'type': 'int', 'name': ''}, '44': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '45': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '46': {'type': 'int', 'name': ''}, '55': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '61': {'type': 'int', 'name': ''}, '66': {'type': 'int', 'name': ''}, '67': {'type': 'int', 'name': ''}, '68': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '71': {'type': 'int', 'name': ''}, '72': {'type': 'int', 'name': ''}, '73': {'type': 'int', 'name': ''}, '74': {'type': 'int', 'name': ''}, '76': {'type': 'int', 'name': ''}, '81': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '8': {'type': 'int', 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'3': {'type': 'message', 'message_typedef': {'3': {'type': 'double', 'name': ''}, '4': {'type': 'double', 'name': ''}}, 'name': ''}, '4': {'type': 'bytes', 'name': ''}, '5': {'type': 'int', 'name': ''}, '6': {'type': 'int', 'name': ''}}, 'name': ''}, '16': {'type': 'bytes', 'name': ''}, '17': {'type': 'message', 'message_typedef': {}, 'name': ''}, '18': {'type': 'int', 'name': ''}, '8': {'type': 'int', 'name': ''}}, 'name': ''}, '3': {'type': 'int', 'name': ''}, '5': {'type': 'message', 'message_typedef': {}, 'name': ''}, '4': {'type': 'bytes', 'name': ''}}, 'name': '', 'alt_typedefs': {'1': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'3': {'type': 'double', 'name': ''}, '4': {'type': 'double', 'name': ''}}, 'name': ''}, '4': {'type': 'bytes', 'name': ''}, '5': {'type': 'int', 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '3': {'type': 'bytes', 'name': ''}, '4': {'type': 'bytes', 'name': ''}, '5': {'type': 'bytes', 'name': ''}}, 'name': ''}, '16': {'type': 'bytes', 'name': ''}, '17': {'type': 'message', 'message_typedef': {}, 'name': ''}, '18': {'type': 'int', 'name': ''}, '8': {'type': 'int', 'name': ''}, '9': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '12': {'type': 'bytes', 'name': ''}}, 'name': ''}, '10': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '4': {'type': 'message', 'message_typedef': {'3': {'type': 'fixed64', 'name': ''}, '4': {'type': 'fixed64', 'name': ''}}, 'name': ''}, '5': {'type': 'int', 'name': ''}, '6': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '3': {'type': 'int', 'name': ''}, '5': {'type': 'bytes', 'name': ''}, '4': {'type': 'bytes', 'name': ''}}}}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}}, 'name': ''}, '4': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '11': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '3': {'type': 'int', 'name': ''}, '4': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '5': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'bytes', 'name': ''}}, 'name': ''}, '6': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '10': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'message', 'message_typedef': {}, 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'5': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'int', 'name': ''}, '5': {'type': 'int', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}}, 'name': ''}}, 'name': ''}}, 'name': '', 'alt_typedefs': {'1': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'bytes', 'name': ''}}}}, '11': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'bytes', 'name': ''}}, 'name': ''}, '14': {'type': 'message', 'message_typedef': {'2': {'type': 'bytes', 'name': ''}, '3': {'type': 'bytes', 'name': ''}, '4': {'type': 'bytes', 'name': ''}, '5': {'type': 'bytes', 'name': ''}}, 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}}, 'name': ''}, '4': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '11': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '3': {'type': 'int', 'name': ''}, '4': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '5': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'bytes', 'name': ''}}, 'name': ''}, '6': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '10': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'message', 'message_typedef': {}, 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'5': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'int', 'name': ''}, '5': {'type': 'int', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}}, 'name': ''}}, 'name': ''}}, 'name': '', 'alt_typedefs': {'1': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'bytes', 'name': ''}}}}, '11': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'bytes', 'name': ''}}, 'name': ''}, '14': {'type': 'message', 'message_typedef': {'2': {'type': 'bytes', 'name': ''}, '3': {'type': 'bytes', 'name': ''}, '4': {'type': 'bytes', 'name': ''}, '5': {'type': 'bytes', 'name': ''}, '1': {'type': 'fixed32', 'name': ''}}, 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}}, 'name': ''}, '4': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}}, 'name': ''}, '4': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '8': {'type': 'message', 'message_typedef': {'2': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'3': {'type': 'fixed64', 'name': ''}, '4': {'type': 'fixed64', 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'3': {'type': 'fixed64', 'name': ''}, '4': {'type': 'fixed64', 'name': ''}}, 'name': ''}}, 'name': ''}}, 'name': ''}, '10': {'type': 'message', 'message_typedef': {'2': {'type': 'bytes', 'name': ''}, '9': {'type': 'int', 'name': ''}, '15': {'type': 'message', 'message_typedef': {'2': {'type': 'bytes', 'name': ''}, '5': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'int', 'name': ''}, '5': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '32': {'type': 'bytes', 'name': ''}, '16': {'type': 'int', 'name': ''}}, 'name': ''}, '15': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}}, 'name': ''}, '6': {'type': 'bytes', 'name': ''}, '7': {'type': 'int', 'name': ''}, '10': {'type': 'int', 'name': ''}, '12': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '5': {'type': 'bytes', 'name': ''}, '10': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '4': {'type': 'bytes', 'name': ''}, '5': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'int', 'name': ''}, '5': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '6': {'type': 'bytes', 'name': ''}, '7': {'type': 'bytes', 'name': ''}, '8': {'type': 'bytes', 'name': ''}, '4': {'type': 'bytes', 'name': ''}}, 'name': ''}, '15': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}, '4': {'type': 'int', 'name': ''}, '9': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'4': {'type': 'int', 'name': ''}}, 'name': ''}, '2': {'type': 'bytes', 'name': ''}}, 'name': ''}, '3': {'type': 'int', 'name': ''}, '4': {'type': 'int', 'name': ''}, '5': {'type': 'int', 'name': ''}}, 'name': ''}, '8': {'type': 'int', 'name': ''}, '5': {'type': 'int', 'name': ''}, '6': {'type': 'message', 'message_typedef': {}, 'name': ''}}, 'name': ''}, '16': {'type': 'int', 'name': ''}, '19': {'type': 'message', 'message_typedef': {'2': {'type': 'bytes', 'name': ''}}, 'name': ''}, '21': {'type': 'int', 'name': ''}, '22': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}, '4': {'type': 'int', 'name': ''}}, 'name': ''}, '23': {'type': 'int', 'name': ''}, '8': {'type': 'int', 'name': ''}, '9': {'type': 'int', 'name': ''}, '13': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'message', 'message_typedef': {'2': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '24': {'type': 'int', 'name': ''}}, 'name': ''}, '5': {'type': 'bytes', 'name': ''}, '4': {'type': 'int', 'name': ''}}, 'name': ''}, '5': {'type': 'message', 'message_typedef': {'5': {'type': 'bytes', 'name': ''}, '6': {'type': 'bytes', 'name': ''}, '1': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '3': {'type': 'bytes', 'name': ''}, '4': {'type': 'bytes', 'name': ''}, '5': {'type': 'bytes', 'name': ''}}, 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'fixed64', 'name': ''}, '2': {'type': 'fixed64', 'name': ''}, '3': {'type': 'fixed64', 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'fixed32', 'name': ''}, '2': {'type': 'fixed32', 'name': ''}, '3': {'type': 'fixed32', 'name': ''}}, 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}, '4': {'type': 'fixed32', 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'3': {'type': 'fixed64', 'name': ''}, '4': {'type': 'fixed64', 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'3': {'type': 'fixed64', 'name': ''}, '4': {'type': 'fixed64', 'name': ''}}, 'name': ''}}, 'name': ''}, '3': {'type': 'message', 'message_typedef': {'3': {'type': 'fixed64', 'name': ''}, '4': {'type': 'fixed64', 'name': ''}}, 'name': ''}, '5': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'fixed64', 'name': ''}, '2': {'type': 'fixed64', 'name': ''}, '3': {'type': 'fixed64', 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'fixed32', 'name': ''}, '2': {'type': 'fixed32', 'name': ''}, '3': {'type': 'fixed32', 'name': ''}}, 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}, '4': {'type': 'fixed32', 'name': ''}}, 'name': ''}}, 'name': ''}, '4': {'type': 'message', 'message_typedef': {'2': {'type': 'bytes', 'name': ''}, '9': {'type': 'int', 'name': ''}, '15': {'type': 'message', 'message_typedef': {'5': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'int', 'name': ''}, '5': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '16': {'type': 'int', 'name': ''}, '32': {'type': 'bytes', 'name': ''}}, 'name': ''}}, 'name': ''}, '10': {'type': 'message', 'message_typedef': {}, 'name': ''}}, 'name': ''}, '4': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '4': {'type': 'int', 'name': ''}, '5': {'type': 'fixed32', 'name': ''}}, 'name': ''}, '3': {'type': 'int', 'name': ''}, '5': {'type': 'int', 'name': ''}, '6': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '7': {'type': 'int', 'name': ''}}, 'name': ''}, '5': {'type': 'bytes', 'name': ''}, '6': {'type': 'bytes', 'name': ''}, '9': {'type': 'int', 'name': ''}, '12': {'type': 'bytes', 'name': ''}, '16': {'type': 'message', 'message_typedef': {'9': {'type': 'int', 'name': ''}, '20': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}}, 'name': ''}}, 'name': ''}, '24': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}}, 'name': ''}}, 'name': ''}, '32': {'type': 'bytes', 'name': ''}}, 'name': ''}, '26': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '3': {'type': 'bytes', 'name': ''}, '4': {'type': 'bytes', 'name': ''}, '7': {'type': 'bytes', 'name': ''}, '8': {'type': 'bytes', 'name': ''}, '9': {'type': 'message', 'message_typedef': {'16428293': {'type': 'fixed64', 'name': ''}}, 'name': ''}, '10': {'type': 'bytes', 'name': ''}, '15': {'type': 'int', 'name': ''}}, 'name': '', 'alt_typedefs': {'1': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '3': {'type': 'bytes', 'name': ''}, '4': {'type': 'bytes', 'name': ''}, '8': {'type': 'bytes', 'name': ''}, '9': {'type': 'bytes', 'name': ''}, '15': {'type': 'int', 'name': ''}}}}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'2': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}, '8': {'type': 'message', 'message_typedef': {'3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '5': {'type': 'message', 'message_typedef': {}, 'name': ''}}, 'name': ''}, '9': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}, '4': {'type': 'int', 'name': ''}}, 'name': ''}, '4': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}}, 'name': ''}, '5': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '4': {'type': 'bytes', 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '27': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '3': {'type': 'bytes', 'name': ''}, '4': {'type': 'bytes', 'name': ''}, '7': {'type': 'bytes', 'name': ''}, '8': {'type': 'bytes', 'name': ''}, '9': {'type': 'message', 'message_typedef': {'16428293': {'type': 'fixed64', 'name': ''}}, 'name': ''}, '10': {'type': 'bytes', 'name': ''}, '15': {'type': 'int', 'name': ''}}, 'name': '', 'alt_typedefs': {'1': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '3': {'type': 'bytes', 'name': ''}, '4': {'type': 'bytes', 'name': ''}, '8': {'type': 'bytes', 'name': ''}, '9': {'type': 'bytes', 'name': ''}, '15': {'type': 'int', 'name': ''}}}}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'2': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}, '8': {'type': 'message', 'message_typedef': {'3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '5': {'type': 'message', 'message_typedef': {}, 'name': ''}}, 'name': ''}, '9': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}, '4': {'type': 'int', 'name': ''}}, 'name': ''}, '4': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}}, 'name': ''}, '5': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '4': {'type': 'bytes', 'name': ''}}, 'name': ''}}, 'name': ''}, '28': {'type': 'message', 'message_typedef': {'13': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {}, 'name': ''}, '3': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '33': {'type': 'int', 'name': ''}, '40': {'type': 'message', 'message_typedef': {}, 'name': ''}, '42': {'type': 'int', 'name': ''}, '46': {'type': 'bytes', 'name': ''}, '47': {'type': 'message', 'message_typedef': {'9': {'type': 'int', 'name': ''}, '13': {'type': 'int', 'name': ''}, '31': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '32': {'type': 'bytes', 'name': ''}}, 'name': ''}, '49': {'type': 'bytes', 'name': ''}}, 'name': ''}, '3': {'type': 'int', 'name': ''}, '4': {'type': 'int', 'name': ''}, '8': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'bytes', 'name': ''}, '4': {'type': 'int', 'name': ''}}, 'name': ''}, '19': {'type': 'message', 'message_typedef': {'3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'5': {'type': 'message', 'message_typedef': {'1': {'type': 'bytes', 'name': ''}, '2': {'type': 'int', 'name': ''}, '5': {'type': 'int', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}}, 'name': ''}}, 'name': ''}}, 'name': ''}, '4': {'type': 'bytes', 'name': ''}}, 'name': ''}, '20': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'bytes', 'name': ''}}, 'name': ''}, '4': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '21': {'type': 'int', 'name': ''}, '24': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'int', 'name': ''}, '4': {'type': 'int', 'name': ''}}, 'name': ''}, '27': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}}, 'name': ''}}, 'name': ''}, '29': {'type': 'int', 'name': ''}, '12': {'type': 'bytes', 'name': ''}}, 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'message', 'message_typedef': {'1': {'type': 'fixed64', 'name': ''}, '2': {'type': 'fixed64', 'name': ''}, '3': {'type': 'fixed64', 'name': ''}}, 'name': ''}, '2': {'type': 'message', 'message_typedef': {'1': {'type': 'fixed32', 'name': ''}, '2': {'type': 'fixed32', 'name': ''}, '3': {'type': 'fixed32', 'name': ''}}, 'name': ''}, '3': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}}, 'name': ''}, '4': {'type': 'fixed32', 'name': ''}}, 'name': ''}, '5': {'type': 'bytes', 'name': ''}}, 'name': ''}}, 'name': ''}, '4': {'type': 'int', 'name': ''}, '5': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'int', 'name': ''}, '3': {'type': 'message', 'message_typedef': {}, 'name': ''}}, 'name': ''}, '6': {'type': 'message', 'message_typedef': {'1': {'type': 'int', 'name': ''}, '2': {'type': 'message', 'message_typedef': {'3': {'type': 'double', 'name': ''}, '4': {'type': 'double', 'name': ''}}, 'name': ''}}, 'name': ''}, '8': {'type': 'int', 'name': ''}}
    
    for file_found in files_found:
        with open(file_found, 'rb') as f:
            data = f.read()
            arreglo = (data)
            pb = arreglo[8:]
            values, types = blackboxprotobuf.decode_message(pb, typess)
        for x, y in values.items():
            #print(x, y)
            if x == '2':
                for data in y.items():
                    startinfo = data[1]['1']['1']['1']['1']
                    latyour = (startinfo['3']['3']) #lat your location
                    longyour = (startinfo['3']['4']) #long your location
                    startloc = ''
                    if '4' in startinfo:
                        startloc = (startinfo['4'].decode()) #your location name
                    if '1' in startinfo:
                        startloc = (startinfo['1'].decode()) #your location address
                    
                    destinfo = data[1]['1']['1-1']['1']['1'];
                    latdest = (destinfo['3']['3']) # dest lat long
                    longdest = (destinfo['3']['4']) # dest long
                    destination=''
                    if '4' in destinfo:
                        destination = (data[1]['1']['1-1']['1']['1']['4'].decode()) #dest name
                    if '1' in destinfo:
                        destination = (data[1]['1']['1-1']['1']['1']['1'].decode()) #dest addresss
                    
                    destdata = (data[1]['1']['12'].decode()) #dest URL with lat longs
                    #ic(data[1]['1']['2'][1]) #list has possible 2 turn by turns [0] &[1]
                    pass
                    
            if x == '4':
                #Stop timestamp
                timeofstop = datetime.fromtimestamp(y/1000, tz=timezone.utc)
                timeofstop = convert_utc_human_to_timezone(timeofstop, time_offset)
                
            if x == '5':
                #Start timestamp
                timeofstart = datetime.fromtimestamp(y['1']/1000, tz=timezone.utc)
                timeofstart = convert_utc_human_to_timezone(timeofstart, time_offset)
                
            if x == '6':
                latstop = y['2']['3'] #lat destination reached or navigation ended
                longstop = y['2']['4'] #lat destination reached or navigation ended                    
            
        data_list.append((timeofstart,'Start',startloc,latyour,longyour,destdata))
        data_list.append((timeofstop,'End',destination,latdest,longdest,''))            
                    
        if len(data_list) > 0:
            report = ArtifactHtmlReport('Google Maps Last Trip')
            report.start_artifact_report(report_folder, f'Google Maps Last Trip')
            report.add_script()
            data_headers = ('Timestamp', 'Directionality', 'Place','Latitude','Longitude','Data')
            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()
            
            tsvname = f'Google Maps Last Trip'
            tsv(report_folder, data_headers, data_list, tsvname)
            
            tlactivity = f'Google Maps Last Trip'
            timeline(report_folder, tlactivity, data_list, data_headers)
            
            kmlactivity = f'Google Maps Last Trip'
            kmlgen(report_folder, kmlactivity, data_list, data_headers)
            
        else:
            logfunc(f'No Google Maps Last Trip available')

__artifacts__ = {
        "googleLastTrip": (
                "GEO Location",
                ('*/com.google.android.apps.maps/files/saved_directions.data.cs'),
                get_googleLastTrip)
}
