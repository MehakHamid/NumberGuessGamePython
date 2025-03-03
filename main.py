{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyPMHtdM+VyBY9XCq2iBXSSd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MehakHamid/NumberGuessGamePython/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2J2YxNQXp_j-",
        "outputId": "29698cda-0282-4a10-e0a4-2fe60447d0c7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🎯 Welcome to the Number Guessing Game! 🎯\n",
            "Guess the number (between 1 and 100). You have 7 attempts.\n",
            "Attempt 1/7: Enter your guess: 7\n",
            "Too low! Try again. ⬆️\n",
            "Attempt 2/7: Enter your guess: 5\n",
            "Too low! Try again. ⬆️\n",
            "Attempt 3/7: Enter your guess: 70\n",
            "Too high! Try again. ⬇️\n",
            "Attempt 4/7: Enter your guess: 50\n",
            "Too low! Try again. ⬆️\n",
            "Attempt 5/7: Enter your guess: 0\n",
            "⚠️ Out of range! Guess a number between 1 and 100.\n",
            "Attempt 5/7: Enter your guess: 80\n",
            "Too high! Try again. ⬇️\n",
            "Attempt 6/7: Enter your guess: 60\n",
            "Too high! Try again. ⬇️\n",
            "Attempt 7/7: Enter your guess: 2\n",
            "Too low! Try again. ⬆️\n",
            "😢 You've used all 7 attempts! The correct number was 51.\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "\n",
        "def number_guessing_game():\n",
        "    secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100\n",
        "    max_attempts = 7  # Limit the number of attempts\n",
        "    attempts = 0\n",
        "    print(\"🎯 Welcome to the Number Guessing Game! 🎯\")\n",
        "    print(\"Guess the number (between 1 and 100). You have 7 attempts.\")\n",
        "\n",
        "    while attempts < max_attempts:\n",
        "        try:\n",
        "            guess = int(input(f\"Attempt {attempts + 1}/{max_attempts}: Enter your guess: \"))\n",
        "        except ValueError:\n",
        "            print(\"❌ Invalid input! Please enter a number between 1 and 100.\")\n",
        "            continue\n",
        "\n",
        "        if guess < 1 or guess > 100:\n",
        "            print(\"⚠️ Out of range! Guess a number between 1 and 100.\")\n",
        "            continue\n",
        "\n",
        "        attempts += 1\n",
        "\n",
        "        if guess < secret_number:\n",
        "            print(\"Too low! Try again. ⬆️\")\n",
        "        elif guess > secret_number:\n",
        "            print(\"Too high! Try again. ⬇️\")\n",
        "        else:\n",
        "            print(f\"🎉 Congratulations! You guessed the correct number {secret_number} in {attempts} attempts. 🎉\")\n",
        "            break\n",
        "    else:\n",
        "        print(f\"😢 You've used all {max_attempts} attempts! The correct number was {secret_number}.\")\n",
        "if __name__ == \"__main__\":\n",
        "    number_guessing_game()\n"
      ]
    }
  ]
}