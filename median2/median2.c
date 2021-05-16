#include <stdio.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size)
{
/* Limit is 1 millon */
#define MIN_INT -2000000
#define MAX_INT 2000000
    int *ns1;
    int ns1Num;
    int *ns2;
    int ns2Num;
    int low, high;
    
    if (nums1Size <= nums2Size) {
        ns1 = nums1;
        ns1Num = nums1Size;
        ns2 = nums2;
        ns2Num = nums2Size;
    } else {
        ns1 = nums2;
        ns1Num = nums2Size;
        ns2 = nums1;
        ns2Num = nums1Size;
    }
    /* Bin sarch on shorter list */
    low = 0;
    high = ns1Num;
    while (low <= high) {
        int part1, part2;
        int minRight1, maxLeft1, minRight2, maxLeft2;
        int maxL, minR;

        part1 = (low + high) / 2;
        part2 = (ns1Num + ns2Num + 1) / 2 - part1;

        maxLeft1 = (part1 == 0) ? MIN_INT : ns1[part1 - 1];
        minRight1 = (part1 == ns1Num) ? MAX_INT : ns1[part1];
        
        maxLeft2 = (part2 == 0) ? MIN_INT : ns2[part2 - 1];
        minRight2 = (part2 == ns2Num) ? MAX_INT : ns2[part2];

        /* Success ? */
        if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
            if ((ns1Num + ns2Num) & 1) {
                /* Odd case */
                return (double) (maxLeft1 >= maxLeft2 ? maxLeft1 : maxLeft2);
            } else {
                /* Even case */
                int maxL, minR;
                double t;
                maxL = maxLeft1 >= maxLeft2 ? maxLeft1 : maxLeft2;
                minR = minRight1 <= minRight2 ? minRight1 : minRight2;

                t = maxL + minR;
                return t / 2.0;
            }
        } else if (maxLeft1 > minRight2) {
            high = part1 - 1;
        } else {
            low = part1 + 1;
        }
    }
    return (double) -1;
}

int main()
{
	{
		int nums1[] = {1, 3};
		int nums2[] = {2};
		printf("%f\n", findMedianSortedArrays(nums1, 2, nums2, 1));
	}
	{
		int nums1[] = {1, 2};
		int nums2[] = {3, 4};
		printf("%f\n", findMedianSortedArrays(nums1, 2, nums2, 2));
	}
}
