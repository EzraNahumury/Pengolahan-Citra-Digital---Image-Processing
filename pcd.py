# 71220848	Priesma Putra Reditama
# 71220849	Ezra Kristanto Nahumury
# 71220914	Glen Daud Crasby Karo Karo
# 71220927	Imanuel Putra Anugerah Faot
# 71220956	Vicky Yohanes Putra Setiawan

#===================================================================================================#




import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_image():
    # load gambar
    img = cv2.imread('g1.jpg')

    # konversi dari BGR ke HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    def get_mask_and_result(lower_range1, upper_range1, lower_range2=None, upper_range2=None):
        # Create mask for the first color range
        mask1 = cv2.inRange(hsv, lower_range1, upper_range1)

        if lower_range2 is not None and upper_range2 is not None:
            # Create mask for the second color range
            mask2 = cv2.inRange(hsv, lower_range2, upper_range2)

            # Combine the masks
            mask_combined = cv2.bitwise_or(mask1, mask2)
        else:
            mask_combined = mask1

        # Apply morphological operations
        kernel = np.ones((5, 5), np.uint8)
        mask_combined = cv2.erode(mask_combined, kernel, iterations=1)
        mask_combined = cv2.dilate(mask_combined, kernel, iterations=1)

        # Apply the combined mask to the original image
        result_combined = cv2.bitwise_and(img, img, mask=mask_combined)

        return mask_combined, result_combined

    while True:
        # Ask user for color choices
        print("Choose your option:")
        print("1. One color")
        print("2. Two colors")
        print("0. Exit")
        option = input("Enter your choice (0, 1, or 2): ")

        if option == '0':
            break

        if option == '1':
            print("Choose a color:")
            print("1. Blue")
            print("2. Red")
            print("3. Orange")
            print("4. Green")
            print("5. Yellow")
            print("6. Purple")
            choice1 = input("Enter your choice (1-6): ")

            if choice1 == '1':
                lower_range1, upper_range1 = np.array([100, 50, 50]), np.array([120, 255, 255])
                color_name1 = 'Blue'
            elif choice1 == '2':
                lower_range1, upper_range1 = np.array([0, 50, 50]), np.array([10, 255, 255])
                lower_range2, upper_range2 = np.array([170, 50, 50]), np.array([180, 255, 255])
                color_name1 = 'Red'
            elif choice1 == '3':
                lower_range1, upper_range1 = np.array([10, 50, 50]), np.array([25, 255, 255])
                color_name1 = 'Orange'
            elif choice1 == '4':
                lower_range1, upper_range1 = np.array([50, 50, 50]), np.array([70, 255, 255])
                color_name1 = 'Green'
            elif choice1 == '5':
                lower_range1, upper_range1 = np.array([20, 50, 50]), np.array([40, 255, 255])
                color_name1 = 'Yellow'
            elif choice1 == '6':
                lower_range1, upper_range1 = np.array([130, 50, 50]), np.array([155, 255, 255])
                color_name1 = 'Purple'
            else:
                print("Invalid choice.")
                continue

            if choice1 == '2':
                mask_combined, result_combined = get_mask_and_result(lower_range1, upper_range1, lower_range2, upper_range2)
            else:
                mask_combined, result_combined = get_mask_and_result(lower_range1, upper_range1)
            color_title = color_name1

            # tampilkan the original image
            plt.subplot(1, 3, 1)
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            plt.title('Original Image')
            plt.axis('off')

            # tampilkan the combined mask
            plt.subplot(1, 3, 2)
            plt.imshow(mask_combined, cmap='gray')
            plt.title(color_title + ' Mask')
            plt.axis('off')

            # tampilkan the combined result
            plt.subplot(1, 3, 3)
            plt.imshow(cv2.cvtColor(result_combined, cv2.COLOR_BGR2RGB))
            plt.title(color_title + ' Result')
            plt.axis('off')

            plt.show()

        elif option == '2':
            print("Choose two colors:")
            print("1. Blue")
            print("2. Red")
            print("3. Orange")
            print("4. Green")
            print("5. Yellow")
            print("6. Purple")
            choice1 = input("Enter your first choice (1-6): ")
            choice2 = input("Enter your second choice (1-6): ")

            if choice1 == choice2:
                print("Please choose two different colors.")
                continue

            if choice1 == '1':
                lower_range1, upper_range1 = np.array([100, 50, 50]), np.array([120, 255, 255])
                color_name1 = 'Blue'
            elif choice1 == '2':
                lower_range1, upper_range1 = np.array([0, 50, 50]), np.array([10, 255, 255])
                lower_range2_1, upper_range2_1 = np.array([170, 50, 50]), np.array([180, 255, 255])
                color_name1 = 'Red'
            elif choice1 == '3':
                lower_range1, upper_range1 = np.array([10, 50, 50]), np.array([25, 255, 255])
                color_name1 = 'Orange'
            elif choice1 == '4':
                lower_range1, upper_range1 = np.array([50, 50, 50]), np.array([70, 255, 255])
                color_name1 = 'Green'
            elif choice1 == '5':
                lower_range1, upper_range1 = np.array([20, 50, 50]), np.array([40, 255, 255])
                color_name1 = 'Yellow'
            elif choice1 == '6':
                lower_range1, upper_range1 = np.array([130, 50, 50]), np.array([155, 255, 255])
                color_name1 = 'Purple'
            else:
                print("Invalid choice.")
                continue

            if choice2 == '1':
                lower_range2, upper_range2 = np.array([100, 50, 50]), np.array([120, 255, 255])
                color_name2 = 'Blue'
            elif choice2 == '2':
                lower_range2, upper_range2 = np.array([0, 50, 50]), np.array([10, 255, 255])
                lower_range2_2, upper_range2_2 = np.array([170, 50, 50]), np.array([180, 255, 255])
                color_name2 = 'Red'
            elif choice2 == '3':
                lower_range2, upper_range2 = np.array([10, 50, 50]), np.array([25, 255, 255])
                color_name2 = 'Orange'
            elif choice2 == '4':
                lower_range2, upper_range2 = np.array([50, 50, 50]), np.array([70, 255, 255])
                color_name2 = 'Green'
            elif choice2 == '5':
                lower_range2, upper_range2 = np.array([20, 50, 50]), np.array([40, 255, 255])
                color_name2 = 'Yellow'
            elif choice2 == '6':
                lower_range2, upper_range2 = np.array([130, 50, 50]), np.array([155, 255, 255])
                color_name2 = 'Purple'
            else:
                print("Invalid choice.")
                continue

            if choice1 == '2':
                mask1, result1 = get_mask_and_result(lower_range1, upper_range1, lower_range2_1, upper_range2_1)
            else:
                mask1, result1 = get_mask_and_result(lower_range1, upper_range1)

            if choice2 == '2':
                mask2, result2 = get_mask_and_result(lower_range2, upper_range2, lower_range2_2, upper_range2_2)
            else:
                mask2, result2 = get_mask_and_result(lower_range2, upper_range2)

            mask_combined = cv2.bitwise_or(mask1, mask2)
            result_combined = cv2.add(result1, result2)
            color_title = color_name1 + ' and ' + color_name2

            # tampilkan  original gambar
            fig, axes = plt.subplots(3, 3, figsize=(6, 6))

            # tampilkan  original gambar
            axes[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            axes[0, 0].set_title('Original Image')
            axes[0, 0].axis('off')

            # tampilkan  hsv
            axes[0, 1].imshow(hsv, cmap='hsv')
            axes[0, 1].set_title('HSV')
            axes[0, 1].axis('off')

            # tampilkan  hsv
            axes[0, 2].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            axes[0, 2].set_title('Original Image')
            axes[0, 2].axis('off')

            # tampilkan the mask 1
            axes[1, 0].imshow(mask1, cmap='gray')
            axes[1, 0].set_title('Mask 1')
            axes[1, 0].axis('off')

            # tampilkan the mask 2
            axes[1, 1].imshow(mask2, cmap='gray')
            axes[1, 1].set_title('Mask 2')
            axes[1, 1].axis('off')

            # tampilkan the combined mask
            axes[1, 2].imshow(mask_combined, cmap='gray')
            axes[1, 2].set_title('Combined Mask')
            axes[1, 2].axis('off')

            # tampilkan the result 1
            axes[2, 0].imshow(cv2.cvtColor(result1, cv2.COLOR_BGR2RGB))
            axes[2, 0].set_title(color_name1)
            axes[2, 0].axis('off')

            # tampilkan result 2
            axes[2, 1].imshow(cv2.cvtColor(result2, cv2.COLOR_BGR2RGB))
            axes[2, 1].set_title(color_name2)
            axes[2, 1].axis('off')

            # tampilkan kombinasi
            axes[2, 2].imshow(cv2.cvtColor(result_combined, cv2.COLOR_BGR2RGB))
            axes[2, 2].set_title(color_title)
            axes[2, 2].axis('off')

            plt.tight_layout()
            plt.show()

        else:
            print("Invalid option.")
            continue


process_image()
