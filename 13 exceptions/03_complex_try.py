def serve_chai(flavor):
    try:
        # This block runs first
        print(f"Preparing {flavor} chai")

        # If flavor is "unknown", we manually raise an error
        if flavor == "unknown":
            raise ValueError("invalid flavor")

    # This block runs only if ValueError occurs
    except ValueError as e:
        print("Error:", e)

    # This block runs only if NO exception occurred
    else:
        print(f"{flavor} is served")

    # This block runs no matter what (error or no error)
    finally:
        print("Next customer please\n")


# Calling the function


serve_chai("masala")
serve_chai("unknown")
