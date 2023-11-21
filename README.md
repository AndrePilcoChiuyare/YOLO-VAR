# YOLO - VAR

This application has been developed to be used in any sport where a ball is needed. This makes it possible to review the plays in detail and be able to rule on fouls or highlight details of the game.

## How to set up the enviroment

- First we create the enviroment `.env`
    ```bash
    python -m venv .env
    ```

- Install `pip`
    ```bash
    python -m pip install --user --upgrade pip
    python -m pip --version
    ```

- Install [PyTorch](https://pytorch.org/get-started/locally/) by selecting your preferences
    ```bash
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    ```
    > This command was used with a dedicated GPU GeForce RTX 3050 (Notebook)

- Install `Ultralytics` library via pip in order to be able to use YOLOv8
    ```bash
    pip install ultralytics
    ```
- Install `Keyboard` library via pip
    ```
    pip install keyboard
    ```

##  How to use

- Once you have the enviroment created and the requirements installed, you can run the Python command
  ```bash
  python VAR.py
  ```

- Now you're able to start reviewing the most important plays of the match using the next keys
```bash
  Space: Zoom-in / Zoom-out
  P: Play / Pause
  W: Increase zoom
  S: Decrease zoom
  A: Rewind
  D: Fast-forward
  Q: Quit
  ```

- If you don't have an own video, you can use [ours](https://www.youtube.com/watch?v=ot2lYbm9izg), download it using `downloadYT.py` in `assets`

> You can find more information at [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com) 