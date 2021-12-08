#include <iostream>
#include <fstream>
#include <vector>
#include <string>

typedef struct s_case
{
	bool status = false;
	int value = -1;
}               t_case;

std::vector<std::string> split(const std::string& str, const std::string& delim)
{
	std::vector<std::string> tokens;
	size_t prev = 0, pos = 0;
	do
	{
		pos = str.find(delim, prev);
		if (pos == std::string::npos) pos = str.length();
		std::string token = str.substr(prev, pos-prev);
		if (!token.empty()) tokens.push_back(token);
		prev = pos + delim.length();
	}
	while (pos < str.length() && prev < str.length());
	return tokens;
}

std::vector<int>    get_input_nbr(std::ifstream &data)
{
	std::string good_number_as_str;

	getline(data, good_number_as_str);

	std::vector<std::string> tmp = split(good_number_as_str, ",");

	std::vector<int> ret;

	for (auto it = tmp.begin(); it != tmp.end(); ++it) {
		ret.push_back(std::stoi(*it));
	}
	return ret;
}

std::vector<t_case>	get_nbr_as_int(std::string &str)
{
	std::vector<std::string> tmp = split(str, " ");

	std::vector<t_case> ret;

	for (auto it = tmp.begin(); it != tmp.end(); ++it) {
		t_case curr;
		curr.value = std::stoi(*it);
		ret.push_back(curr);
	}

	return ret;
}

int	check_valid_grid(std::vector<std::vector< std::vector<t_case> > > &all_grid) {
	int j = 0;

	for (auto grid = all_grid.begin(); grid != all_grid.end(); ++grid) {
		for (int i = 0; i < 5; ++i) {
			j = 0;
			while ((*grid)[i][j].status == true) {
				++j;
				if (j == 5) {
					return (grid - all_grid.begin());
				}
			}
			j = 0;
			while ((*grid)[j][i].status == true) {
				++j;
				if (j == 5) {
					return (grid - all_grid.begin());
				}
			}
		}
	}
	return -1;
}

int calculate_score(std::vector< std::vector<t_case> > grid, int new_number) {
	int marked = 0;
	int non_marked = 0;

	for (int i = 0; i < 5; ++i) {
		for (int j = 0; j < 5; ++j) {
			std::cout << grid[i][j].value << "|" << grid[i][j].status << " ";
			if (grid[i][j].status == true) {
				marked += grid[i][j].value;
			}
			else {
				non_marked += grid[i][j].value;
			}
		}
		std::cout << "\n";
	}
	return new_number * non_marked;
}

int main()
{
	std::ifstream data("./data");

	std::vector<int> numbers = get_input_nbr(data);

	std::vector<std::vector< std::vector<t_case> > > all_grid;

	std::string current_line;

	while (getline(data, current_line)) {
		if (current_line.length() != 0) {
			auto row = get_nbr_as_int(current_line);
			all_grid.rbegin()->push_back(row);
		}
		else {
			all_grid.resize(all_grid.size() + 1);
		}
	}
	
	for (auto it_nbr = numbers.begin(); it_nbr != numbers.end(); ++it_nbr) {
		if (check_valid_grid(all_grid) == -1) {
			for (auto grid = all_grid.begin(); grid != all_grid.end(); ++grid) {
				for (auto row = (*grid).begin(); row != (*grid).end(); ++row) {
					for (auto curr_case = (*row).begin(); curr_case != (*row).end(); ++curr_case) {
						if ((*curr_case).value == *it_nbr) {
							(*curr_case).status = true;
						}
					}
				}
			}
		}
		else {
			std::cout << calculate_score(all_grid[check_valid_grid(all_grid)], *(it_nbr - 1)) << std::endl;
			return 0;
		}
	}
}