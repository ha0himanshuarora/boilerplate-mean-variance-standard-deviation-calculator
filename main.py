from mean_var_std import calculate
def pretty_print(result):
    for key,value in result.items():
        print(f"\n {key.capitalize()}:")
        print(f"\n Columns (axis=0): {value[0]}:")
        print(f" Rows (axis=2): {value[1]}:")
        print(f" Flattened: {value[2]}:")
    print("\n"+"-"*50+"\n")

if __name__=="__main__":
    data=[0,1,2,3,4,5,6,7,8]
    print(f"Input Data: {data}")
    try:
        result=calculate(data)
        pretty_print(result)
    except Exception as e:
        print(f"Error: {e}")

