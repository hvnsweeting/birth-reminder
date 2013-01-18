from ConfigParser import SafeConfigParser
import utils

FILENAME = "birthrmd.cfg"


def parse_config(FILENAME):
    scpr = SafeConfigParser()
    scpr.read(utils.fix_path(FILENAME))

    SMTP_SERVER  = scpr.get("smtp", "server")
    SMTP_PORT = scpr.get("smtp", "port")
    USERNAME = scpr.get('account', 'username')
    PASSWORD = scpr.get('account', 'password')
    CSVPATH = utils.fix_path(scpr.get("file", "mails_data"))

    return {'user': USERNAME,
            'passwd': PASSWORD,
            'server': SMTP_SERVER,
            'port': SMTP_PORT,
            'csv_path': CSVPATH}


_CFG_ = parse_config(FILENAME)

if __name__ == "__main__":
    print _CFG_
