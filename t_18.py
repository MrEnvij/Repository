
def readPolinon(file):
    try:
        coefs = {}
        with open(file) as f:
            for line in f:
                power, coef = line.split()
                power = int(power)
                coef = float(coef)
                coefs[power] = coef

        return coefs
    except FileNotFoundError: # якщо файл не знайдений
        print("File not found")
        return None
    except ValueError:
        print("Something went wrong")
        return None
    except IOError:
        print("IOError")
        return None
    except TypeError:
        print("&&")

####### main ###########

if __name__ == '__main__':
    polinom = readPolinon('polinom.txt')
    print(polinom)