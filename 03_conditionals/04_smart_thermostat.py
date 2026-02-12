device_status = "active"
temp = 34
# device_status → state flag (string-based)
# temp → numeric value used for threshold comparison

if device_status == "active":
    # outer condition acts as a gate
    # inner logic executes only if device is active

    if temp > 35:
        # threshold check
        # strict comparison (35 not included)
        print("Warn:High temp")
    else:
        print("Temp is normal")

else:
    # executes when device_status != "active"
    print("Device is Offline")
