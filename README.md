# Virtual Mouse Using Hand Tracking

## Introduction
**Virtual Mouse using Hand Tracking** is a desktop application created with Python 3.8 that uses hand gestures to control a computer. Instead of relying on traditional pointing devices like optical or wireless mice, the application captures video from a webcam with a resolution of at least 0.9 Megapixels and a 60 Hz display. It processes this input to recognize the user’s hand and the gestures made, allowing for mouse operations without physical devices.

## Objective
The objective of this project is to provide a smart, gesture-based alternative to traditional mouse usage, enhancing user convenience and comfort by removing the dependency on physical pointing devices. The application aims to improve accessibility for users facing challenges with standard mice.

## Working Overview
The application captures video from the user's webcam using OpenCV, processes the frames with the MediaPipe library to detect hand landmarks, and recognizes predefined gestures. Depending on the gesture detected, it performs corresponding mouse operations using PyAutoGui and AutoPy. The application can be exited by pressing 'q' on the keyboard.

## Operations
- **Cursor Drag:** Triggered by raising the index finger while keeping the thumb and middle finger down.
- **Left Click:** Executed when both the thumb and index finger are raised with the distance between their tips below a defined threshold.
- **Right Click:** Performed when both the index and middle fingers are raised under the same distance condition.

## Tech Stack
- **Programming Language:** Python 3.8
- **Libraries:** 
  - OpenCV
  - MediaPipe
  - PyAutoGui
  - AutoPy
