# USB Cold Storage Signing
To use these files we must firs consider how USB signing will work. First the udev service in linux recognizes a device has been mounted. The udev service then calls the systemd and spawns off another service that calls our pointer script. This pointer script directs use finally to the signing script which waits for a mount and then signes the transactions in that directory with the specified wallet from electrum.
<br/><br/>Put more simply:
identifyUSB.rules -> sign_usb.service -> point_electrum.sh -> sign_electrum.sh
<br/><br/>Make sure to read these files yourself and update any paths that do not match.
<br/><br/>The two service files belong under:
~~~
/etc/udev/rules.d/identifyUSB.rules
/etc/systemd/system/isign_usb.service
~~~
  While the point_electrum and sign_electrum files belong in the 
~~~
/home/linaro/electrum-smart/point_electrum.sh
/home/linaro/electrum-smart/sign_electrum.sh
~~~
Furthermore:
Both of the sh files need to be tagged as executable in order to be ran by the service
~~~
sudo chmod +x point_electrum.sh
sudo chmod +x sign_electrum.sh
~~~

After a quick reboot, the cold storage should work.

It is important to note that when using electrum, the coldstorage wallet must match the public wallet that created it.
Namely, if the public wallet is only a single address, the coldstorage wallet must also only have one private address when signing.
When any electrum-smart command is called (./electrum-smart) we can denote the wallet with -w (path to wallet)

