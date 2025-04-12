def convert(feet, inches):
    meters = round(float(feet) * 0.3048 + float(inches) * 0.0254, 3)
    print(f"Calculated Meter from External Call: {meters}")
    return meters


if __name__ == "__main__":
    meters = convert("6", "3")



