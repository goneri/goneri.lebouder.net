+++
title = "Elixir: xmerl/include/xmerl.hrl could not be found"
date = 2022-09-04T23:51:52+00:00
+++
I recently faced this error when trying to build an Elixir project.

`== Compilation error in file lib/swoosh/adapters/xml/helpers.ex ==  
** (ArgumentError) lib file xmerl/include/xmerl.hrl could not be found  
(elixir 1.13.4) lib/record/extractor.ex:41: Record.Extractor.from_lib_file/1  
(elixir 1.13.4) lib/record/extractor.ex:18: Record.Extractor.from_or_from_lib_file/1  
(elixir 1.13.4) lib/record/extractor.ex:5: Record.Extractor.extract/2  
lib/swoosh/adapters/xml/helpers.ex:5: (module)  
(elixir 1.13.4) lib/kernel/parallel_compiler.ex:346: anonymous fn/5 in Kernel.ParallelCompiler.spawn_workers/7  
could not compile dependency :swoosh, "mix compile" failed. Errors may have been logged above. You can recompile this dependency with "mix deps.compile swoosh", update it with "mix deps.update swoosh" or clean it with "mix deps.clean swoosh"`

If you can the error above on Fedora, you probably need to install the `erlang-xmerl` package.
