class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        visited=[0]*n
        queue=deque([start])

        while queue:
            index=queue.popleft()

            if arr[index]==0:
                return True
            
            # Jump forward
            forward = index + arr[index]
            if 0 <= forward < n and not visited[forward]:
                visited[forward] = True
                queue.append(forward)

            # Jump backward
            backward = index - arr[index]
            if 0 <= backward < n and not visited[backward]:
                visited[backward] = True
                queue.append(backward)
        return False
