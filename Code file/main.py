import sys

if __name__ == "__main__":
    if "--api" in sys.argv:
        from api.app import app
        app.run(host="0.0.0.0", port=5000)
    else:
        from gui.tkinter_app import ObjectRecognition
        ObjectRecognition().run()
