{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN/LefXAWGON63tCMVN6sgF",
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
        "<a href=\"https://colab.research.google.com/github/siissioe12/aesarfag-fg-afb/blob/main/Untitled0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "eBNwtYobR2b3"
      },
      "outputs": [],
      "source": [
        "import pygame\n",
        "import sys\n",
        "\n",
        "# Marco, usa i commenti.\n",
        "# Se usiamo i commenti ci capiamo meglio\n",
        "# Ah, le variabili (se ne metti) dagli nomi che hanno senso e sono umani (Es. Variabile che definisce i soldi che ho in banca = soldi).\n",
        "# Non chiamarla (la variabile) code tipo \"<sdfgaernadrbaefnaetbalfivnsfdvuaysdbvuyafbauhvilbhadufbe7rhgvihalelvhulnvHILFHn\" Ok?\n",
        "\n",
        "# Inizializza Pygame\n",
        "pygame.init()\n",
        "\n",
        "# Imposta le dimensioni della finestra\n",
        "larghezza, altezza = 1920, 1080\n",
        "\n",
        "# Crea la finestra\n",
        "finestra = pygame.display.set_mode((larghezza, altezza), pygame.RESIZABLE)\n",
        "\n",
        "# Imposta il titolo della finestra\n",
        "pygame.display.set_caption(\"ROTFL\")\n",
        "\n",
        "# Stato iniziale a schermo intero\n",
        "fullscreen = False\n",
        "\n",
        "# Loop principale\n",
        "while True:\n",
        "    for evento in pygame.event.get():\n",
        "        if evento.type == pygame.QUIT:\n",
        "            # Chiudi la finestra e esci dal programma\n",
        "            pygame.quit()\n",
        "            sys.exit()\n",
        "        elif evento.type == pygame.KEYDOWN:\n",
        "            if evento.key == pygame.K_F6:\n",
        "                # Cambia a schermo intero o finestra\n",
        "                fullscreen = not fullscreen\n",
        "                if fullscreen:\n",
        "                    pygame.display.set_mode((larghezza, altezza), pygame.FULLSCREEN)\n",
        "                else:\n",
        "                    pygame.display.set_mode((larghezza, altezza), pygame.RESIZABLE)\n",
        "\n",
        "    # Aggiorna la finestra\n",
        "    pygame.display.flip()"
      ]
    }
  ]
}