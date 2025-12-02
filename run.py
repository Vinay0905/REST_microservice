from app import create_app

def main():
    app = create_app()
    # keep debug True if you want debugger, but disable reloader which caused duplicate imports
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

if __name__ == "__main__":
    main()
