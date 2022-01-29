# deauthentication-attack-using-python

The objective is to target the communication between router and the device(Victim) and effectively disabling the WiFi on the victim device.
To achieve this we use something called a “deauthentication frame”. When a client wishes to disconnect from the Access Point, the client sends the deauthentication frame. 
The AP also sends the deauthentication frame in the form of a reply. This is the normal process, but an attacker can take advantage of this process. 
So how could this be implemented? Simple, The attacker spoofs the MAC address of the victim and sends the deauthentication frame(or deauth frame) to AP(Router) on behalf of the victim; because of this, the connection with the victim is dropped. 
Deauthentication frames can be sent in the clear (no encryption) and therefore, anyone within range of the victim’s LAN can spoof the MAC address of the victim or AP and disconnect a client from the network.

Code explanation: 
First we take all necessary values needed(like AP MAC , victim’s MAC..) as command line arguments, and based on the value of count mentioned we are calling the specified function(if no value for count is mentioned, we perform infinite deauth if mentioned we send that no of frames). 
Check_interface function checks if the particular interface supports monitor mode or packet injection, so whether we can transmit the packets or not. 
The function(deauth and inf_deauth) creates a 802.11(Wi-Fi) frame using the Dot11, RadioTap and Dot11Deauth classes defined in the Scapy package. The Dot11 class allows us to create an 802.11 packet. 
To send deauthentication frames we need to set the following Dot11 object properties: addr1, addr2 ,addr3 . addr1 is set to the MAC address of the victim machine; addr2 is set to the AP’s MAC address; and addr3 is also set to the MAC address of the AP .The Dot11Deauth class adds all the necessary details to our 802.11 frame that specifies that this will be a deauthentication frame. 
Then sendp function allows us to send the packet we created via a specified interface (iface), specify the number of times we want to send our packet (count), and how long the interval will be between each sent packet (inter).
