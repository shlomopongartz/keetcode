#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

struct queue {
	char **words;
	int len;
};

int dist(char *w1, char *w2, int len)
{
	int diff = 0;
	char *c1;
	char *c2;
	int i;

	c1 = w1;
	c2 = w2;

	for (i = 0; i < len; ++i) {
		if (*c1 != *c2) {
			if (diff)
				return 2;
			++diff;
		}
		++c1;
		++c2;
	}
	return diff;
}

int ladderLength(char * beginWord, char * endWord, char ** wordList, int wordListSize)
{
	bool foundLast;
	int i, j, k, ind;
	struct queue queues[2];
	int level;
	int len = strlen(beginWord);

	foundLast = false;
	for (i = 0; i < wordListSize; i++) {
		if (strcmp(wordList[i], endWord) == 0) {
			foundLast = true;
			break;
		}
	}
	if (!foundLast)
		return 0;

	queues[0].words = malloc(wordListSize * 2 * sizeof(char *));
	queues[0].words[0] = beginWord;
	queues[0].len = 1;
	queues[1].words = queues[0].words + wordListSize;
	queues[1].len = 0;
	level = 1;
	ind = 0;
	while (queues[ind].len > 0) {
		++level;
		queues[1 - ind].len = 0;
		for (i = 0; i < queues[ind].len; ++i) {
			k = 0;
			for (j = 0; j < wordListSize; ++j) {
				if (dist(queues[ind].words[i],
				         wordList[j],
				         len) == 1) {
					if (strcmp(wordList[j], endWord) == 0) {
						free(queues[0].words);
						return level;
					}

					queues[1 - ind].words[queues[1 - ind].len] = wordList[j];
					++queues[1 - ind].len;
				} else {
					wordList[k] = wordList[j];
					++k;
				}
			}
			wordListSize = k;
		}
		ind = 1 - ind;
	}
	free(queues[0].words);
	return 0;
}


int main()
{
	{
		char *beginWord = "hit";
		char *endWord = "cog";
		char *wordList[] = {"hot","dot","tog","cog"};
		int exp = 0;
		int  res = ladderLength(beginWord, endWord, wordList, sizeof(wordList)/sizeof(wordList[0]));
		printf("exp = {%d} result = {%d}\n", exp, res);

	}
	{
		char *beginWord = "hit";
		char *endWord = "cog";
		char *wordList[] = {"hot", "dot", "dog", "lot", "log", "cog"};
		int exp = 5;
		int  res = ladderLength(beginWord, endWord, wordList, sizeof(wordList)/sizeof(wordList[0]));
		printf("exp = {%d} result = {%d}\n", exp, res);
	}
	{
		char *beginWord = "hit";
		char *endWord = "cog";
		char *wordList[] = {"hot", "dot", "dog", "lot", "log"};
		int exp = 0;
		int  res = ladderLength(beginWord, endWord, wordList, sizeof(wordList)/sizeof(wordList[0]));
		printf("exp = {%d} result = {%d}\n", exp, res);
	}
}
