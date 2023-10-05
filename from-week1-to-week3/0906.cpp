#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <algorithm>

int main() {
    const int NUM_VALUES = 1'000'000;
    std::vector<int> scores;

    std::srand(static_cast<unsigned int>(std::time(nullptr))); // 랜덤 시드 설정

    for(int i = 0; i < NUM_VALUES; ++i) {
        scores.push_back((std::rand() % 100) + 1); // 1~100 사이의 점수
    }

    // 점수를 내림차순으로 정렬
    std::sort(scores.rbegin(), scores.rend());

    // 각 등급의 커트라인을 구함
    int grade1_cut = scores[0.04 * NUM_VALUES - 1]; // 0-4%
    int grade2_cut = scores[0.11 * NUM_VALUES - 1]; // 4-11%
    int grade3_cut = scores[0.23 * NUM_VALUES - 1]; // 11-23%
    int grade4_cut = scores[0.40 * NUM_VALUES - 1]; // 23-40%

    std::cout << "1등급 커트라인: " << grade1_cut << std::endl;
    std::cout << "2등급 커트라인: " << grade2_cut << std::endl;
    std::cout << "3등급 커트라인: " << grade3_cut << std::endl;
    std::cout << "4등급 커트라인: " << grade4_cut << std::endl;

    return 0;
}
