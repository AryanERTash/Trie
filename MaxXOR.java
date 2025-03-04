// Leetcode 1707

import java.util.*;

class BitUtils {
	public static int getNthBit(int num, int n) {
		// n is 0 based index from LSB
		return (num >> n) & 1;
	}
}

class NumLimitPair implements Comparable<NumLimitPair> {
	public int num;
	public int limit;
	public int index;

	public NumLimitPair(int num, int limit, int index) {
		this.num = num;
		this.limit = limit;
		this.index = index;
	}

	@Override
	public int compareTo(NumLimitPair pair2) {
		return Integer.compare(this.limit, pair2.limit);
	}

}

class Trie {
	public Trie[] links;

	public Trie() {

		this.links = new Trie[2];

	}

	public void insert(int num) {
		Trie current = this;

		for (int i = 31; i >= 0; i--) {
			int bit = BitUtils.getNthBit(num, i);

			if (current.links[bit] == null) {
				current.links[bit] = new Trie();
			}

			current = current.links[bit];
		}

	}

	public boolean isEmpty() {
		return this.links == null || (this.links[0] == null && this.links[1] == null);
	}

	public int getMaxXorNum(int num) {
		// asumes at least one entry per tries prior to getting max xor

		Trie current = this;

		int second = 0;

		for (int i = 31; i >= 0; i--) {

			int bit = BitUtils.getNthBit(num, i);
			int compbit = 1 - bit;

			if (current.links[compbit] != null) {
				second = second | (compbit << i);
				current = current.links[compbit];
			} else {
				second = second | (bit << i);
				current = current.links[bit];
			}
		}

		return second;
	}
}

class Solution {
	public int[] maximizeXor(int[] nums, int[][] queries) {
		Arrays.sort(nums);

		Queue<NumLimitPair> queryQueue = new PriorityQueue<>();

		for (int i = 0; i < queries.length; i++) {
			queryQueue.add(new NumLimitPair(queries[i][0], queries[i][1], i));
		}

		int[] result = new int[queries.length];
		Trie t = new Trie();

		int numIndex = 0;

		while (!queryQueue.isEmpty()) {
			NumLimitPair nlPair = queryQueue.poll();

			for (int i = numIndex; i < nums.length && nums[i] <= nlPair.limit; i++) {

				t.insert(nums[i]);
				numIndex++;

			}

			if (t.isEmpty()) {
				result[nlPair.index] = -1;
			} else {
				result[nlPair.index] = t.getMaxXorNum(nlPair.num) ^ nlPair.num;
			}

		}

		return result;

	}
}