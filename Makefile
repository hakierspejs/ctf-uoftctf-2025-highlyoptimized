CFLAGS += -I.
# disable warnings, they're noise here
CFLAGS += -w
# if DEBUG is defined, set -DDEBUG
ifdef DEBUG
CFLAGS += -DDEBUG
endif
all: highlyoptimized
