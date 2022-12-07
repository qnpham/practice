/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  let result;
  const nums3 = [];
  nums1.forEach((e) => {
    nums3.push(e);
  });
  nums2.forEach((e) => {
    nums3.push(e);
  });
  nums3.sort((a, b) => b - a);
  if (nums3.length % 2 !== 0) {
    result = nums3[Math.floor(nums3.length / 2)];
  } else {
    result =
      (nums3[Math.floor(nums3.length / 2) - 1] +
        nums3[Math.floor(nums3.length / 2)]) /
      2;
  }
  return result;
};
