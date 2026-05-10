{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPvwzn/OLDzW3iA3ndkR7X4",
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
        "<a href=\"https://colab.research.google.com/github/siddharthasiriparapu/python1/blob/main/Functions_10.5.26_1and2\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kGCmOzo2ikwT",
        "outputId": "f4fa7ac9-04f1-4a5e-e90b-2b72e506846b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hi\n",
            "I hope you're fine today\n"
          ]
        }
      ],
      "source": [
        "def well():\n",
        "  print(\"Hi\")\n",
        "  print(\"I hope you're fine today\")\n",
        "\n",
        "well()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def weather():\n",
        "  print('The weather is great in:', city)\n",
        "  print('We have', x ,\"hier\")\n",
        "  print(\"How is it there?\")\n",
        "\n",
        "city = \"halle\"\n",
        "x = \"summer\"\n",
        "weather()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ms_2v6f6lbWB",
        "outputId": "8f4f527a-305c-476c-c159-6945617bbd79"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The weather is great in: halle\n",
            "We have summer hier\n",
            "How is it there?\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def my_function(name, place):\n",
        "    print(name, place)\n",
        "\n",
        "my_function(\"siddhartha\" , \"rohit\")\n",
        "my_function(\"ram\" ,\"tilak\")#we can type any thing"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A-2qAG0pznAD",
        "outputId": "52dba01f-2fd9-4aa5-df06-8b5913ad1382"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "siddhartha rohit\n",
            "ram tilak\n"
          ]
        }
      ]
    }
  ]
}
