//@category Export
//@keybinding
//@menupath
//@toolbar

import ghidra.app.decompiler.*;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.*;
import ghidra.util.task.ConsoleTaskMonitor;

import java.io.FileWriter;
import java.io.IOException;

public class ExportDecompiledCode extends GhidraScript {

    @Override
    protected void run() throws Exception {
        if (currentProgram == null) {
            println("No program loaded.");
            return;
        }

        String outputPath = askString("Output Path", "Enter the path to save the decompiled code:");

        DecompInterface decompiler = setupDecompiler(currentProgram);
        if (decompiler == null) {
            println("Unable to initialize decompiler.");
            return;
        }

        try (FileWriter writer = new FileWriter(outputPath)) {
            FunctionIterator functions = currentProgram.getFunctionManager().getFunctions(true);
            for (Function function : functions) {
                DecompileResults results = decompiler.decompileFunction(function, decompiler.getOptions().getDefaultTimeout(), monitor);
                ClangTokenGroup decomp = results.getC();
                writer.write(decomp.toString() + "\n\n");
            }
        } catch (IOException e) {
            println("Error writing to file: " + e.getMessage());
        }

        println("Decompiled code exported to: " + outputPath);
    }

    private DecompInterface setupDecompiler(Program program) {
        DecompInterface decompiler = new DecompInterface();
        decompiler.openProgram(program);

        DecompileOptions options = new DecompileOptions();
        options.setOutputLanguage("C");
        decompiler.setOptions(options);

        decompiler.toggleCCode(true);
        decompiler.toggleSyntaxTree(true);

        return decompiler;
    }
}
