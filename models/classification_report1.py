{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "connected-signature",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import itertools\n",
    "\n",
    "\n",
    "def plot_classification_report(classificationReport,\n",
    "                               title='Classification report',\n",
    "                               cmap='RdBu'):\n",
    "\n",
    "    classificationReport = classificationReport.replace('\\n\\n', '\\n')\n",
    "    classificationReport = classificationReport.replace(' / ', '/')\n",
    "    lines = classificationReport.split('\\n')\n",
    "\n",
    "    classes, plotMat, support, class_names = [], [], [], []\n",
    "    for line in lines[1:]:  # if you don't want avg/total result, then change [1:] into [1:-1]\n",
    "        t = line.strip().split()\n",
    "        if len(t) < 2:\n",
    "            continue\n",
    "        classes.append(t[0])\n",
    "        v = [float(x) for x in t[1: len(t) - 1]]\n",
    "        support.append(int(t[-1]))\n",
    "        class_names.append(t[0])\n",
    "        plotMat.append(v)\n",
    "\n",
    "    plotMat = np.array(plotMat)\n",
    "    xticklabels = ['Precision', 'Recall', 'F1-score']\n",
    "    yticklabels = ['{0} ({1})'.format(class_names[idx], sup)\n",
    "                   for idx, sup in enumerate(support)]\n",
    "\n",
    "    plt.imshow(plotMat, interpolation='nearest', cmap=cmap, aspect='auto')\n",
    "    plt.title(title)\n",
    "    plt.colorbar()\n",
    "    plt.xticks(np.arange(3), xticklabels, rotation=45)\n",
    "    plt.yticks(np.arange(len(classes)), yticklabels)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
