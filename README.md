# YOLO - ImageProcessing

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

##  How to use

- Once you have the enviroment created and the requirements installed, you can run the Python command
  ```bash
  python yolo.py
  ```

> You can find more information at [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com) 