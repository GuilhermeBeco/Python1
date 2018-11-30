   #!/bin/bash
    VAR1=${1?Error: no file given}
    python3 -c 'from '$VAR1' import * ; main()'
