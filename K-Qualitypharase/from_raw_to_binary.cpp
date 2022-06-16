//use helper.h header file which is in utils folder
#include "utils/helper.h"
#include <cassert>

const string ENDINGS = ".!?,;:()\"[]";

int main(int argc, char* argv[])
//we give input as RawData file and this code generate its binary code
{
	if (argc != 1) {
		cerr << "[Usage] <input raw file> <output binary file>" << endl;
		return -1;
	}
//reading the given input file
	FILE* in = tryOpen("RawData.txt", "r");
	vector<string> sentences;
	for (;getLine(in);) {
		string sentence = "";
		for (int i = 0; line[i]; ++ i) {
			char ch = tolower(line[i]);
			if (ENDINGS.find(ch) != -1) {
				if (sentence.size() > 0) {
					sentences.push_back(sentence);
				}
				sentence = "";
			} else {
				if (!isalpha(ch)) {
                    if (ch == '\'') {
                        sentence += ch;
                    } else if (sentence.size() > 0 && sentence[sentence.size() - 1] != ' ') {
						sentence += ' ';
					}
				} else {
					sentence += ch;
				}
			}
		}
		if (sentence.size() > 0) {
			sentences.push_back(sentence);
		}
	}
	fclose(in);

	cerr << "# Sentences = " << sentences.size() << endl;

	unordered_set<string> tokens;
	FOR (sentence, sentences) {
		vector<string> temp = splitBy(*sentence, ' ');
		FOR(iter, temp) {
			tokens.insert(*iter);
		}
        assert(tokens.size() != 0);
	}
	vector<string> unigrams(tokens.begin(), tokens.end());

	cerr << "# Unigrams = " << unigrams.size() << endl;
//generate binary code of all the words
//this file generate the file name as sentences.buf

	FILE* out = tryOpen("sentences.buf", "wb");

	Binary::write(out, sentences.size());
	FOR (sentence, sentences) {
		Binary::write(out, *sentence);
	}

	Binary::write(out, unigrams.size());
	FOR (unigram, unigrams) {
		Binary::write(out, *unigram);
	}
	fclose(out);

	return 0;
}

