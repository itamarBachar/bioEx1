import math

# from matplotlib import pyplot as plt


def check_input(input_text):
    for i in input_text:
        # cast the input to float and check if it is a number\
        try:
            float(i)
        except ValueError:
            return False
    # check if the first input is a number and is not between 0 and 1
    if float(input_text[0]) < 0 or float(input_text[0]) > 1:
        return False
    # go over for 2 to 5 and check if there sum is 1
    if sum([float(input_text[i]) for i in range(2, 6)]) != 1:
        return False
    return True


# def plot_results(most_rumor_itreation, p, l, s1, s2, s3, s4):
#     print(most_rumor_itreation)
#     # devide all numbers by 5000 to get the percentage
#     for elment in range(len(most_rumor_itreation)):
#         most_rumor_itreation[elment] = float(most_rumor_itreation[elment] / 5000) * 100
#     # plot the results
#     # put headline of the values of p L s1 s2 s3 s4
#     plt.title("p = " + str(p) + " L = " + str(l) + " s1 = " + str(s1) + " s2 = " + str(s2) + " s3 = " + str(
#         s3) + " s4 = " + str(s4))
#     plt.plot(most_rumor_itreation)
#     plt.xlabel('Iteration')
#     plt.ylabel('Precentage of people who heard the rumor')
#     plt.show()
#
#
# def plot_results2(most_rumor_itreation, flag):
#     # Step 1
#     sums = [0] * len(most_rumor_itreation[0])
#     for lst in most_rumor_itreation:
#         for i in range(len(lst)):
#             sums[i] += lst[i]
#
#     # Step 2
#
#     for i in range(len(sums)):
#         sums[i] = sums[i] / flag
#
#     plt.plot(sums)
#     plt.xlabel('Iteration')
#     plt.ylabel('New Person Expose')
#     plt.show()


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx * dx + dy * dy)
