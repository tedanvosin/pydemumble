/* Minimal hand-maintained stub of LLVM's generated llvm-config.h.

   Upstream generates this from llvm-config.h.cmake at build time; a plain
   source checkout has no build dir, so pydemumble ships this stub instead.
   pydemumble links the demanglers statically, so the export-annotation macros
   (LLVM_ENABLE_LLVM_EXPORT_ANNOTATIONS) are intentionally left undefined,
   which yields empty visibility annotations. See
   src/third_party/THIRD_PARTY_NOTICES.md. */
#ifndef LLVM_CONFIG_H
#define LLVM_CONFIG_H

#define LLVM_ENABLE_THREADS 1
#define LLVM_HAS_ATOMICS 1
#define LLVM_VERSION_MAJOR 21
#define LLVM_VERSION_MINOR 0
#define LLVM_VERSION_PATCH 0
#define LLVM_VERSION_STRING "21.0.0"

#endif
