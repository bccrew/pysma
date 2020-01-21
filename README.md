pysma library
=============

[![image](https://circleci.com/gh/kellerza/pysma.svg?style=svg)](https://circleci.com/gh/kellerza/pysma)
[![Codecov](https://codecov.io/gh/kellerza/pysma/branch/master/graph/badge.svg)](https://codecov.io/gh/kellerza/pysma)

This is my personal fork of the SMA Webconnect library for Python 3. The library was originally created
by Johann Kellerman to integrate SMA with HomeAssistant.

See <http://www.sma-solar.com> for more information on the SMA solar
inverters

This fork aims to document my own invertor, the Sunny Boy 4.0 AV-41. It has webconnect 1.5 and uses a self signed-ssl certificate. It can send output to any MQTT broker.

Example usage
=============

See [example.py](./example.py) for a basic usage and tests

python3 example.py https://ipaddress user password

Home Assistant
==============

The Home Assistant sma sensor documentation can be found
[here](https://www.home-assistant.io/components/sma)

By default ssl is disabled (Sunnyboy 1.5 WebConnect uses `http://`). If
you access your SMA WebConnect via `https://` you should set both
`ssl: true` and `verify_ssl: false`.

Daily usage is not always available from the SMA WebConnect interface.
It is possible to get around this by using a
[utility meter](https://www.home-assistant.io/components/utility_meter)


Sunny Boy 4.0 AV-41 (probably all AV-41 models)
===============================================

Listed below is a table representing all instantaneous values that are currently offered by the Sunny Boy 4.0 AV-41. 
This way, you can add your own sensors in the __init.py__ file after you installed the pysma library.

| **Sensor** | **Value** | **Json** |
| --- | --- | --- |
| **1.) Status** |
| **1.1) Operation** |
| Waiting time until feed-in | ------- | 6100_00416600 |
| Condition | Ok | 6180_08214800 |
| Operating status | Derating | 6180_08412800 |
| Grid relay status | Closed | 6180_08416400 |
| Derating | not active | 6180_08416500 |
| **1.2) PV system control** |
| Status | On | 6180_08413300 |
| **1.3) Device control** |
| Status | On | 6180_08413200 |
| **1.4) Device status** |
| Ok | 4,000 W | 6100_00411E00 |
| Warning | 0 W | 6100_00411F00 |
| Fault | 0 W | 6100_00412000 |
| **1.5) Inverter** |
| Condition | Ok | 6180_08414C00 |
| **1.6) Current event** |
| Event number manufacturer | ------- | 6100_00418000 |
| Message | none | 6180_08414900 |
| Recommended action | none | 6180_08414A00 |
| Fault correction measure | none | 6180_08414B00 |
| **1.7) Update** |
| Status | ------- | 6180_08412900 |
|  |  |  |
| **2.) Device** |
| **2.1) Operation** |
| Backup mode status | Grid mode | 6180_08436800 |
|  |  |  |
| **3.) DC Side**
| **3.1) DC measurements** |
| Power [A] | 0 W | 6380_40251E00_0 |
| Power [B] | 0 W | 6380_40251E00_1 |
| Voltage [A] | 275.14 V | 6380_40451F00_0 |
| Voltage [B] | 275.36 V | 6380_40451F00_1 |
| Current [A] | 0.000 A | 6380_40452100_0 |
| Current [B] | 0.000 A | 6380_40452100_1 |
|  |  |  |
| **4.) AC Side** |
| **4.1) Grid measurements** |
| Power | 14 W | 6100_40263F00 |
| Grid frequency | 50.00 Hz | 6100_00465700 |
| Excitation type of cosPhi | Overexcited | 6180_08465A00 |
| **4.2) Phase currents** |
| Phase L1 | 0.591 A | 6100_40465300 |
| Phase L2 | ------- | 6100_40465400 |
| Phase L3 | ------- | 6100_40465500 |
| **4.3) Phase voltage** |
| Phase L1 | 235.30 V | 6100_00464800 |
| Phase L2 | ------- | 6100_00464900 |
| Phase L3 | ------- | 6100_00464A00 |
| Phase L1 against L2 | ------- | 6100_00464B00 |
| Phase L2 against L3 | ------- | 6100_00464C00 |
| Phase L3 against L1 | ------- | 6100_00464D00 |
| **4.3) Power per phase** |
| Phase L1 | 14 W | 6100_40464000 |
| Phase L2 | ------- | 6100_40464100 |
| Phase L3 | ------- | 6100_40464200 |
| **4.4) PV generation** |
| PV generation power | 14 W | 6100_0046C200 |
| Meter count and PV gen. meter | 92,783 Wh | 6400_0046C300 |
| **4.5) Measured values** |
| Total yield | 92,783 Wh | 6400_00260100 |
| Operating time | 66.69 h | 6400_00462E00 |
| Feed-in time | 64.20 h | 6400_00462F00 |
| **4.6) Grid measurements** |
| Supplied power | ------- | 6100_40463600 |
| Power absorbed | ------- | 6100_40463700 |
| Displacement power factor | ------- | 6100_00464E00 |
| Grid frequency | ------- | 6100_00468100 |
| Apparent power | ------- | 6100_00468100 |
| Reactive power | ------- | 6100_4046F100 |
| Total yield | 0 Wh | 6400_00462400 |
| Absorbed energy | 0 Wh | 6400_00462400 |
| Total energy fed by device | 0 Wh | 6400_00462400 |
| Total energy absorbed from the grid by the device | 0 Wh | 6400_00469200 |
| **4.7) Phase currents** |
| Phase L1 | ------- | 6100_40466500 |
| Phase L2 | ------- | 6100_40466500 |
| Phase L3 | ------- | 6100_40466500 |
| **4.8) Phase voltage** |
| Phase L3 against L1 | ------- | 6100_00467700 |
| Phase L1 against L2 | ------- | 6100_00467800 |
| Phase L2 against L3 | ------- | 6100_00467900 |
| Phase L1 | ------- | 6100_0046E500 |
| Phase L2 | ------- | 6100_0046E600 |
| Phase L3 | ------- | 6100_0046E700 |
| **4.9) Apparent power** |
| Phase L1 | ------- | 6100_40466C00 |
| Phase L2 | ------- | 6100_40466D00 |
| Phase L3 | ------- | 6100_40466E00 |
| **4.10) Reactive power** |
| Phase L1 | ------- | 6100_4046EE00 |
| Phase L2 | ------- | 6100_4046EF00 |
| Phase L3 | ------- | 6100_4046F000 |
| **4.11) Power per phase** |
| Phase L1 | ------- | 6100_0046E800 |
| Phase L2 | ------- | 6100_0046E900 |
| Phase L3 | ------- | 6100_0046EA00 |
| **4.12) Absorbed phase power** |
| Phase L1 | ------- | 6100_0046EB00 |
| Phase L2 | ------- | 6100_0046EC00 |
| Phase L3 | ------- | 6100_0046ED00 |
| **4.13) Operation** |
| Mains connection | Public electricity mains | 6180_0846A600 |
|  |  |  |
| **5.) Measured values** |
| **5.1) WLAN** | |
| Signal strength of the selected network | 0 | 6100_004AB600 |
