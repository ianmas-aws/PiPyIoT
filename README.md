# AWS IoT Python SDK Demo using Raspberry Pi Sense Hat

### Prerequisites

Install the AWS IoT Python SDK from here: https://github.com/aws/aws-iot-device-sdk-python

Raspbery Pi Sense Hat and Sense Hat SDK from: https://www.raspberrypi.org/products/sense-hat/


### Instructions

1. Clone this repo onto your Pi
2. Edit runShadowEcho.sh to point at the correct location for your root-CA, device certificate and device private key. These are created and can be downloaded when you create & connect your device in the AWS IoT console 
3. Make sure the device name on line 154 of `ThingShadowEcho.py` matches your device name in the AWS IoT console 
4. `chmnd +x runShadowEcho.sh`
5. `./runShadowEcho.sh`
6. Log into the AWS IoT console, find your device and update the shadow. Example shadow shown below:

```{
  "desired": {
    "sequence": "r,on,y,off,r"
  },
  "reported": {
    "sequence": "r,on,y"
  }
}```

Permissable values in `"sequence":` are defined in lightColorList.py 
