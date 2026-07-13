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


# --- Rust (legacy, pre-v0) ---

def test_rust_legacy_print():
	assert pydemumble.demangle("_ZN3std2io5stdio6_print17hc00c8cbe9793b80aE") == \
		"std::io::stdio::_print"


def test_rust_legacy_main():
	assert pydemumble.demangle("_ZN4main17h05444b57a54e5c13E") == "main"


def test_rust_legacy_generic():
	assert pydemumble.demangle(
		"_ZN71_$LT$Test$u20$$u2b$$u20$$u27$static$u20$as$u20$foo..Bar$LT$Test$GT$$GT$3bar17h1234567890abcdefE"
	) == "<Test + 'static as foo::Bar<Test>>::bar"


def test_rust_legacy_closure():
	assert pydemumble.demangle("_ZN28_$u7b$$u7b$closure$u7d$$u7d$17h1234567890abcdefE") == \
		"{{closure}}"


def test_rust_legacy_ref():
	assert pydemumble.demangle("_ZN5$RF$x17h1234567890abcdefE") == "&x"


def test_rust_legacy_no_hash_with_escapes():
	assert pydemumble.demangle("_ZN5$LT$x3fooE") == "<x::foo"


def test_rust_legacy_escapes():
	assert pydemumble.demangle("_ZN4$SP$17h1234567890abcdefE") == "@"
	assert pydemumble.demangle("_ZN4$BP$17h1234567890abcdefE") == "*"
	assert pydemumble.demangle("_ZN4$LP$17h1234567890abcdefE") == "("
	assert pydemumble.demangle("_ZN4$RP$17h1234567890abcdefE") == ")"
	assert pydemumble.demangle("_ZN3$C$17h1234567890abcdefE") == ","


def test_rust_legacy_macos_underscore():
	assert pydemumble.demangle("__ZN4main17h05444b57a54e5c13E") == "main"


def test_rust_legacy_plain_cpp_falls_to_itanium():
	# Plain C++ symbol must NOT match rust legacy; Itanium demangles it.
	assert pydemumble.demangle("_ZN3foo3barE") == "foo::bar"


def test_rust_legacy_hash_only_falls_to_itanium():
	# Single hash-only segment rejected by rust legacy, falls to Itanium.
	assert pydemumble.demangle("_ZN17h1234567890abcdefE") == "h1234567890abcdef"


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
