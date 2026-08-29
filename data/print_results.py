#!/usr/bin/env python3
"""Print classification results and optionally misclassified images."""


def print_results(results_dic, results_stats, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """Print summary statistics and requested misclassified images."""
    print("\n*** Results Summary for CNN Model Architecture", model, "***")
    print("Number of Images:    ", results_stats["n_images"])
    print("Number of Dog Images:        ", results_stats["n_dogs_img"])
    print("Number of a Not a Dog Images:", results_stats["n_notdogs_img"])
    print("\nPercentage of Correct Dogs:         ", results_stats["pct_correct_dogs"])
    print("Percentage of Correct Breed:        ", results_stats["pct_correct_breed"])
    print("Percentage of Correct \"Not-a\" Dog:", results_stats["pct_correct_notdogs"])

    if "pct_match" in results_stats:
        print("Percentage of Correct Matches: ", results_stats["pct_match"])

    incorrect_dog_assignments = any(
        image_data[3] != image_data[4] for image_data in results_dic.values()
    )
    if print_incorrect_dogs and incorrect_dog_assignments:
        print("\n*** Incorrect Dog/Not-Dog Assignments ***")
        for image_data in results_dic.values():
            if image_data[3] != image_data[4]:
                print("Pet Image Label:", image_data[0])
                print("Classifier Label:", image_data[1])
                print()

    if print_incorrect_breed:
        print("\n*** Misclassified Breeds ***")
        for image_data in results_dic.values():
            if image_data[3] == 1 and image_data[2] == 0:
                print("Pet Image Label:", image_data[0])
                print("Classifier Label:", image_data[1])
                print()
