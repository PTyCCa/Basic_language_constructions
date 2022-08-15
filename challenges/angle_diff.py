"""Write a diff function that takes two angles (int)
and returns the smallest difference between them.
Angles can be specified as negative or very large (1000 degrees!).
Remember that arithmetic over angles is modular (modulo 360)."""


def diff(angle1, angle2):
    return min(
        (angle1 - angle2) % 360,
        (angle2 - angle1) % 360,
    )


def diff_ver2(first_angle, second_angle):
    res = min(
      abs(
        first_angle - second_angle),
      abs(
          (first_angle - second_angle) % 360,
          ),
          )
    res2 = min(
      abs(
        second_angle - first_angle),
      abs(
          (second_angle - first_angle) % 360,
          ),
          )
    return min(res, res2)
