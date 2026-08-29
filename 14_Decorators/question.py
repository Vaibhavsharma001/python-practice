# Write a decorator @check_login that checks whether a user is logged in before allowing them to access a function.

# Requirements:
# Create a variable is_logged_in = True/False.
# Create a decorator called check_login.
# If is_logged_in is True, execute the original function.
# If False, print "Please login first!" and do not execute the function.
# Apply the decorator to a function dashboard().

is_logged_in = True

def check_login(func):

    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Please login first!")

    return wrapper


@check_login
def dashboard():
    print("Welcome to Dashboard!")


dashboard()