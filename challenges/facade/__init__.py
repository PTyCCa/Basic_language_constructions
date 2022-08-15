"""The programmer who worked on the project before you scattered all the functions related to mathematical calculations in different modules named numbers1, numbers2 and numbers3 (located, fortunately, in the same solution package). And I also made the names of the functions strange: all functions in the numbers2 module end in two, for example, sum2.

You quickly realized that this is inconvenient and you need to create a single interface to access them (they say "facade"). To do this, you need to import all functions from all the listed modules into the solution / __ init__.py module.

The task is for the file solution / __ init__.py to import all the functions from the three modules described above and expose them to the outside (listed in the __all__ list) under the following names: power (), add (), sub (), sqrt ( ) and mul ().

This assignment does not specifically say where which function is and under what name it lies. The goal of this activity is to get you familiar with the package and module system, which will greatly simplify your life later on. Huge request not to spy on the solution and think on your own, and if something happens, ask a question in the community."""  # noqa E301

from challenges.facade.numbers1 import mul1 as mul
from challenges.facade.numbers2 import add2 as add
from challenges.facade.numbers2 import power2 as power
from challenges.facade.numbers2 import sub2 as sub
from challenges.facade.numbers3 import sqrt3 as sqrt

__all__ = (  # noqa: WPS410
    'add',
    'mul',
    'power',
    'sqrt',
    'sub',
)
