# Test cases ported from demumble's demumble_test.py.
#
# demumble is a command-line tool; pydemumble exposes a single demangle()
# function, so only the "symbol -> demangled string" cases apply. Each is its
# own test below.

import pydemumble


# --- Itanium C++ ---

def test_itanium_function():
	assert pydemumble.demangle("_Z4funcPci") == "func(char*, int)"


def test_itanium_void_function_f():
	assert pydemumble.demangle("_Z1fv") == "f()"


def test_itanium_void_function_g():
	assert pydemumble.demangle("_Z1gv") == "g()"


def test_itanium_destructor():
	assert pydemumble.demangle("_ZN2zx7channelD4Ev") == "zx::channel::~channel()"


def test_itanium_lambda():
	assert pydemumble.demangle("_ZZ3fooiENK3$_0clEi") == \
		"foo(int)::$_0::operator()(int) const"


def test_itanium_operator_new():
	# leading-underscore (macOS) form
	assert pydemumble.demangle("__Znwi") == "operator new(int)"


def test_itanium_bare_type():
	assert pydemumble.demangle("Pi") == "int*"


def test_itanium_block_invoke():
	assert pydemumble.demangle("___Z10blocksNRVOv_block_invoke") == \
		"invocation function for block in blocksNRVO()"


# --- Rust (v0) ---

def test_rust_align_of():
	assert pydemumble.demangle("_RINvNtC3std3mem8align_ofdE") == \
		"std::mem::align_of::<f64>"


def test_rust_nested():
	assert pydemumble.demangle("_RNvNvC5mylib3foo3bar") == "mylib::foo::bar"


# --- Swift ---

def test_swift_old_mangling():
	assert pydemumble.demangle("_TtP3foo3bar_") == "foo.bar"


def test_swift_new_mangling():
	assert pydemumble.demangle("$sSS5countSivg") == \
		"Swift.String.count.getter : Swift.Int"


# --- Microsoft (MSVC) ---

def test_msvc_function_pointer():
	assert pydemumble.demangle("?Fxi@@YAHP6AHH@Z@Z") == \
		"int __cdecl Fxi(int (__cdecl *)(int))"


def test_msvc_move_constructor():
	assert pydemumble.demangle("??0S@@QEAA@$$QEAU0@@Z") == \
		"public: __cdecl S::S(struct S &&)"


def test_msvc_string_literal():
	assert pydemumble.demangle("??_C@_02PCEFGMJL@hi?$AA@") == '"hi"'


def test_msvc_rtti():
	assert pydemumble.demangle(".?AVNet@@") == \
		"class Net `RTTI Type Descriptor Name'"
