# QuecPython AI Chatbot Based on Douyin WebRTC

## Table of Contents

- [Introduction](#Introduction)
- [Features](#Features)
- [Quick_Start](#Quick_Start)
  - [Prerequisites](#Prerequisites)
  - [Installation](#Installation)
  - [Running_ Application](#Running_Application)
- [Directory_Structure](#Directory_Structure)
- [Contributing](#Contributing)
- [License](#License)
- [Support](#Support)

## Introduction

QuecPython introduces an AI chatbot solution based on Douyin WebRTC. This solution utilizes the Volcano RTC library and requires firmware that supports TiktokRTC functionality.

The following module models support this feature:

| Series | Models                   |
| :----- | :----------------------- |
| EC600M | EC600MCN_LE              |
| EC800M | EC800MCN_LE, EC800MCN_GB |
| EG810M | EG810MCN_GA_VOLTE        |

## Features

- Supports agent switching.
- Supports voice tone switching.
- Supports ASR subtitles.
- Supports TTS subtitles.
- Supports voice interruption/barge-in.
- Supports server address switching.
- Supports voice wake-up.
- Uses Python for easy secondary development.

## Quick_Start

### Prerequisites

Before you begin, ensure you have the following prerequisites:

- **Hardware:**

  - [EC600MCNLE QuecPython Standard Development Board](https://python.quectel.com/doc/Getting_started/zh/evb/ec600x-evb.html) (including antenna, Type-C cable, etc.)

    > - View the development board's [schematic](https://images.quectel.com/python/2023/05/EC600X_EVB_V3.2-SCH.pdf) and [silkscreen](https://images.quectel.com/python/2023/05/EC600X_EVB_V3.2-丝印.pdf) documents.
    > - [Purchase link on Quectel Mall](https://www.quecmall.com/goods-detail/2c90800c916a8eb501918d85528b017b)

  - Computer (Windows 7, Windows 10, or Windows 11)

  - LCD Display

    - Model: ST7789
    - Resolution: 240×240
    - [Purchase link on Quectel Mall](https://www.quecmall.com/goods-detail/2c90800b9488359c01951d6700700116)

  - Speaker

    - Any 2-5W power speaker will suffice
    - [Purchase link on Quectel Mall](https://www.quecmall.com/goods-detail/2c90800c94028da201948249e9f4012d)

- **Software:**

  - QuecPython module USB driver: [QuecPython_USB_Driver_Win10_ASR](https://images.quectel.com/python/2023/04/Quectel_Windows_USB_DriverA_Customer_V1.1.13.zip)
  - Debugging tool [QPYcom](https://images.quectel.com/python/2022/12/QPYcom_V3.6.0.zip)
  - QuecPython [firmware](https://github.com/QuecPython/AIChatBot-Volcengine-webRTC/releases/download/v1.0.0/EC600MCNLER06A01M08_OCPU_QPY_TEST0213.zip)
  - Python text editor (e.g., [VSCode](https://code.visualstudio.com/), [Pycharm](https://www.jetbrains.com/pycharm/download/))

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/QuecPython/AIChatBot-Volcengine-webRTC.git
   cd AIChatBot-Volcengine-webRTC
   ```

2. **Install the USB driver.**

3. **Flash the firmware:**
   Follow the [instructions](https://python.quectel.com/doc/Application_guide/zh/dev-tools/QPYcom/qpycom-dw.html#%E4%B8%8B%E8%BD%BD%E5%9B%BA%E4%BB%B6) to flash the firmware onto the development board.

> Note: The Volcano dialogue token in the firmware is for temporary testing and may be revoked at any time. For a better experience, contact Quectel technical support.
> If you have your own Volcano token, you can configure it directly using the `tiktok.config` interface.

### Running_Application

1. **Connect the hardware:**
   Follow the diagram below for hardware connections:
   <img src="docs/zh/media/wire_connection.jpg" style="zoom:67%;" />
   1. Connect the speaker to the pins labeled `SPK+` and `SPK-`.
   2. Connect the LCD screen to the pins labeled `LCD`.
   3. Insert a usable Nano SIM card in the designated slot.
   4. Connect the antenna to the antenna connector labeled `LTE`.
   5. Use a Type-C cable to connect the development board to your computer.
2. **Download the code to the device:**
   - Launch the QPYcom debugging tool.
   - Connect the data cable to the computer.
   - Press the **PWRKEY** button on the development board to power on the device.
   - Follow the [instructions](https://python.quectel.com/doc/Application_guide/zh/dev-tools/QPYcom/qpycom-dw.html#%E4%B8%8B%E8%BD%BD%E8%84%9A%E6%9C%AC) to import all files from the `code` folder into the module's file system, preserving the directory structure.
3. **Run the application:**
   - Select the `File` tab.
   - Choose the `ai_main.py` script.
   - Right-click and select `Run` or use the `Run` shortcut button to execute the script.
4. **Reference run log:**

```python
import example
>>> example.exec('/usr/ai_main.py')
window show over
volume: 6
>>> lte network normal
ai task running

# Press KEY1 to enter the agent
rtc_queue key event 1
start rtc
TIKTOK_RTC_EVENT_START
TIKTOK_RTC_EVENT_TTS_TEXT Hello
TIKTOK_RTC_EVENT_TTS_TEXT Hello, how
TIKTOK_RTC_EVENT_TTS_TEXT Hello, how can
TIKTOK_RTC_EVENT_TTS_TEXT Hello, how can I
TIKTOK_RTC_EVENT_TTS_TEXT Hello, how can I help
TIKTOK_RTC_EVENT_TTS_TEXT Hello, how can I help you
TIKTOK_RTC_EVENT_TTS_TEXT Hello, how can I help you today?

# Press KEY2 to exit the agent
rtc_queue key event 2
stop rtc
```

## Directory_Structure

```plaintext
solution-AI/
├── code/
│   ├── ai_main.py
│   ├── datetime.py
│   ├── ...
│   └── img/
│       ├── battery/
│       │   ├── bat_00.png
│       │   ├── bat_01.png
│       │   └── ...
│       ├── signal/
│       │   ├── signal_00.png
│       │   ├── signal_01.png
│       │   └── ...
│       ├── image1.png
│       ├── image2.png
│       └── ...
├── examples/
│   └── examples_ai.py
├── docs/zh/media/
│           └── wire_connection.jpg
├── EC600MCNLER06A01M08_OCPU_QPY_TEST0213.zip
├── LICENSE
├── readme.md
└── readme_zh.md
```

## Contributing

We welcome contributions to improve this project! Follow these steps to contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the Apache License. See the [LICENSE](https://license/) file for details.

## Support

If you have any questions or need support, refer to the [QuecPython documentation](https://python.quectel.com/doc) or open an issue in this repository.
