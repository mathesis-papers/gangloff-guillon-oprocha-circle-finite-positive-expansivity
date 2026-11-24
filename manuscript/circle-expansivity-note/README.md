# Circle expansivity: extending Gangloff, Guillon and Oprocha's interval obstruction

Haobo Ma (ChronoAI Pte Ltd, Singapore), then Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore).

Licensed under Creative Commons Attribution 4.0 International, `cc-by-4.0`.

The note extends the interval obstruction and doubling method of Gangloff, Guillon and Oprocha to answer their Question 3.1, arXiv:2310.17241v1, Section 3, page 7: no strict finite positive-expansivity level above one occurs for continuous selfmaps of the whole circle. These maps are precisely the topological conjugates of integer power maps of absolute degree at least two. The classification under ordinary positive expansivity is classical; the note deduces it from the finite Bowen bound. It also proves the periodic embedded-circle consequence and the bouquet examples already given in the posing source.

## Build

The bibliography is included in `note.tex`. Use Tectonic 0.17.0:

```sh
tectonic --untrusted note.tex
```

Alternatively, run `pdflatex note.tex` twice with the standard LaTeX packages named in its preamble. No separate bibliography program is needed. `note.pdf` accompanies the source package.

Run the finite exact-arithmetic checks with Python 3:

```sh
python3 verify.py > verification.json
```

There are 3,555 checks: 62 power-map constants, 513 cardinal identities and inequalities, 965 quotient-metric translation identities, and 2,015 geometric-series identities. They concern the displayed algebraic estimates; the topological conclusions have written proofs in the note.

## Coverage and formal sources

`coverage.json` identifies the source items and distinguishes the negative answer, consequences not separately posed, prior results, and questions outside the classification. `metadata.json` gives the authors, license, stable note identity, and mathematical scope.

At scientific revision `71b4d849a96f7050cd0e6270e1551e061c680e33`, the declaration `D5.S1.Dynamics.Shadowing.CircleFinitePositiveExpansiveness.positivelyExpansive_of_finitelyPositiveExpansive` has exactly the continuous whole-circle, uniform finite strict infinite-time Bowen hypothesis and the positive-expansivity conclusion. The same file's `isLocallyInjective_of_finitelyPositiveExpansive` and `surjective` give those consequences. The PDF links each of the six relevant fixed-revision Lean files and identifies its scope. The classification, periodic embedded-circle consequence, and bouquet calculation are written deductions, not additional assertions of those declarations.

The formal source is [CircleFinitePositiveExpansiveness.lean](https://github.com/the-omega-institute/trureturing/blob/71b4d849a96f7050cd0e6270e1551e061c680e33/D5/S1/Dynamics/Shadowing/CircleFinitePositiveExpansiveness.lean).

The other one-dimensional continua in Question 3.2, and the symbolic questions of Question 4.1, are not classified by the circle theorem. The interval and Hawaiian-earring obstructions and the bouquet examples retain their attribution to the posing authors. The classical finite-domain obstruction for injective positively expansive maps is cited to Coven and Keane's 2006 proof, which credits Schwartzman's 1952 dissertation.
