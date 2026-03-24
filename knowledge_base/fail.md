# FAIL Knowledge Base

All rules that have returned FAIL verdict.
Auto-updated after every validation run.

---

## R002 — Drawings must be correct scale in all sheets
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-18 15:10
- **Pages checked:** 3, 4, 5
- **Reference image:** 1-Scale.png
- **Evidence:** Sheet M8398-G2 (Overall Site Plan) uses scale 1:1500, which is classified as 'Not Preferred' per the standard drawing scale reference. Sheet M8398-G3 detail uses 1:200 (Standard/Preferred) and Sheet M8398-G3-2 uses 1:25 (Acceptable), both of which comply. The 1:1500 scale on M8398-G2 should be highlighted as it does not meet the preferred or acceptable scale standards.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R003 — FC stamp is correctly mentioned to all sheets?
- **Verdict:** FAIL
- **Drawing:** input.pdf
- **Last seen:** 2026-03-24 12:53
- **Pages checked:** 0, 1, 2
- **Reference image:** 2-Draft.png
- **Evidence:** DRAFT watermark is not visible on any of the three FC drawing pages provided. All pages show 'FOR CONSTRUCTION' stamp instead. The reference image clearly shows a red 'DRAFT' watermark that should be present on all sheets, but it is absent from pages H8099-00, H8099-G1, and H8099-G2.
- **Times seen:** 6
- **Confidence:** 0.572 🔴 Low

---


## R005b — Child CAD template layer format
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-18 15:10
- **Pages checked:** 3, 4, 5
- **Reference image:** 4-Child CAD template Layer format.png
- **Evidence:** In the FC drawing, proposed/new elements (e.g., 'PROPOSED EWP SET UP LOCATION', 'NEW MERCS#2 SIGNAGE', 'INSTALL NEW VODAFONE NOKIA FYGC GPS ANTENNA', 'NEW JURALCO WALKWAY/HANDRAIL') appear in the same unbold text weight as existing elements. Per the child CAD template rule, proposed/new items must use bold layers while existing items use unbold layers. The drawings do not show this distinction — both existing and new annotation text appear in uniform non-bold weight throughout all pages.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R007 — Work authority number is correct
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 2-Work Authority ID -1.png
- **Evidence:** The Work Authority Number in the FC drawing is 540268 (shown as 'OPTUS WORK AUTHORITY Nº 540268' on the cover sheets), but the reference image (Antenna System tab Scope of Works) shows WA ID 658102. The numbers do not match.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R012 — Service stream site only - Add  “SAED_DA/DC/L3/LO CONDITIONS” in reference documents (Refer snip 8 in next sheet for details)
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** 9-SS-SAED.png
- **Evidence:** The drawing shows ServiceStream as the vendor (indicated by ServiceStream logo and DISTRIBUTION section listing 'SERVICE STREAM: SAMMA TABASSUM'). However, the REFERENCE DOCUMENTS section on page M8398-01 does not include 'SAED_DA/DC/L3/LO CONDITIONS'. The reference documents listed are: OSD-100, OSD-171-2, OSD-171-3, OSD-900, VPL-SC-101810, CERT_JK398, and 'FOR INDARA INFRASTRUCTURE & ENGINEERING DATED 02-04-2025', but 'SAED_DA/DC/L3/LO CONDITIONS' is missing as required for ServiceStream vendor sites.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R017 — Point 1 "Existing structure sections" Mention existing tower with heights, model & Owner. Like below format; EXISTING INDARA 54.76m HIGH ROAM RT84 SELF SUPPORTING LATTICE TOWER
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 2
- **Reference image:** 2-Existing structure sections TITLE.png
- **Evidence:** Drawing section 'EXISTING INDARA ROOFTOP SITE' does not follow the required format. Missing: (1) specific height measurement, (2) model number, (3) structure type designation. Required format per rule: 'EXISTING [OWNER] [HEIGHT]m HIGH [MODEL] [STRUCTURE TYPE]'. Current text only states 'EXISTING INDARA ROOFTOP SITE' without height, model, or complete structure type and owner name.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R021 — Is the antenna maintenance access by EWP only or access step pegs with Lad Saf?. If Lad-saf are present at existing, please check which is certified or not. (Point 5)
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 7-Existing structure sections.png
- **Evidence:** The FC drawing (M8398-G1, point 4 under Existing Indara Rooftop Site) states antenna maintenance access is via 'LADDER AND STEP PEGS WITH FALL ARREST SYSTEM,' and construction access notes reference a Lad-Saf cable on site. However, the drawing does not confirm whether the Lad-Saf/fall arrest system is certified or not, which is required per the rule when Lad-Saf is present at the existing site.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R030 — Update Corrosion Protection note on G1 page. (Only Servicestream site)
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 14-Corrosion protection.png
- **Evidence:** The G1 page (M8398-G1) of this ServiceStream site does not contain a CORROSION PROTECTION section. The reference image shows a required CORROSION PROTECTION note with CORROSIVITY CATEGORY AS/NZS 2312.2 and PROPOSED CORROSION PROTECTION SYSTEM fields, but no such section is present on the FC drawing's G1 page.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R062 — Calculate RF tail length for all RRUs - please consider horizontal & vertical distance for tail calculation
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 5, 6, 7, 8, 9
- **Reference image:** Tail length calculation 1.png
- **Evidence:** The FC drawing does not include any RF tail length calculations for the RRUs. From the elevation drawing (M8398-G4), passive antennas are at EL 15.00m while RRUs range from EL 12.20m down to EL 9.10m, giving vertical distances of 2.8m to 5.9m. RRUs at EL 9.10m have a vertical gap of ~5.9m from the passive antenna, which already exceeds the 5m limit before adding horizontal run and bending radius. The reference image requires explicit annotation of horizontal distance + vertical distance + bending allowance = total RF tail length, and client approval notation if >5m. None of these calculations or annotations are present in the FC drawing pages (G3, G3-2, G3-3, G4).
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R070 — AC units working conditions
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 6-AC issue.png
- **Evidence:** The reference image clearly shows a water leakage issue from the AC unit that was identified by the SDV Engineer. However, the FC drawing page provided (Equipment Shelter Layout Plan M8398-F1) does not contain any notation, callout, or highlight indicating this AC unit water leakage issue. The drawing fails to document the working condition problem that was captured in the field photos.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R080 — Mention PDT approved version number. Please make sure use recent PDT tools
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 15-PDT version number.png
- **Evidence:** No PDT approved version number is mentioned anywhere in the FC drawing pages reviewed (M8398-00, M8398-01, M8398-G1). The reference image shows that the drawing should include a statement such as 'OPTUS POWER TOOL V12.7 APPROVED' in the notes/specifications section, but this is absent from the FC drawing.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R081 — Ensure the exact AC power supply value is mentioned, and it must align with the PVA, power meter photos, and SLD. Also, confirm if a power upgrade is required
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 16-AC power supply.png
- **Evidence:** The FC drawing (M8398-G1) states the existing AC power supply is 40A 3-Phase and requires an upgrade to 63A. However, the PVA report confirms the Optus supply is 50A 3-Phase (meter SN:218038715, 50A protection/main switch rating), and the PDT AC Power Summary shows existing capacity of 50A is sufficient for the proposed upgrade with no upgrade required. The stated 40A value does not align with the PVA, and the power upgrade statement contradicts both the PVA and PDT findings.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R009 — Drawings listed in cover sheet aligned with previous As-built & proposed scope (Sheet name/Number/title/Rev.)
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** 5-Cover sheet - Sheetname-Number-Rev-title.png
- **Evidence:** The FC drawing cover sheet (M8398-00) lists drawings with revisions ranging from B to AB1, but the rule requires the proposed revision to be marked as REV 'A'. The current drawing package shows multiple previous revisions (B, AB, AB1, etc.) which should either be removed if not applicable to the current project, or if this is a continuation, the new revision should be clearly marked as 'A'. Additionally, without access to the previous As-built file, the alignment of sheet names, numbers, titles, and revisions cannot be verified against the prior version. The drawing shows historical revisions are retained rather than being cleaned up for this FC package.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R010 — MERC signage is shown in the FC pack as per the latest Optus OSD requirements - Site specific for typical ground site - OSD-171-1, Rooftop/watertower OSD-171-2 & Site signage legend and notes OSD-171-3.
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** 6-standard OSD sheet.png
- **Evidence:** Drawing shows OSD-171-2 and OSD-171-3 in the reference documents section (page M8398-01), but the site specifications (page M8398-G1) confirm this is a rooftop site ('EXISTING INDARA ROOFTOP SITE'). However, OSD-171-1 is also listed in the reference documents alongside OSD-171-2, when according to the rule, only OSD-171-2 should be included for rooftop sites. OSD-171-3 is correctly included as mandatory for all projects. The inclusion of OSD-171-1 alongside OSD-171-2 for a rooftop site is incorrect per the stated requirement.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R011 — Add reference documents - Add Pole & Mount Structural cert which dates matches with provided cert. Also check with FC issue date
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** 8-Cover sheet certificate 2.png
- **Evidence:** Reference Documents page lists 'CERT_M8398' with 'SUPPLIER STRUCTURAL DESIGN CERTIFICATE - ROOFTOP FOR INDARA INFRASTRUCTURE & ENGINEERING DATED 02-04-2025' but the cover sheet shows no matching pole and mount certificate. The reference document lists a rooftop structural certificate dated 02-04-2025, however, there is no Pole & Mount Structural certificate listed in the Reference Documents section. The certificate name and date cannot be verified as matching because the Pole & Mount certificate is not present in the drawing.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R013 — Distribution list: (Optus & either CPS or Servicestrem)
OPTUS               : SUHAIB OBAID
CPS TECH          : BRETT THOMSON
Service stream: SAMINA TABASSUM
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** 10-distribution list.png
- **Evidence:** Distribution list shows only OPTUS (SUHAIB OBAID) and SERVICE STREAM (SAMINA TABASSUM). Missing CPS TECH entry with BRETT THOMSON. The reference requires three entries: Optus, CPS Tech, and Service Stream. The drawing only lists Optus and ServiceStream, with no CPS Tech representative listed.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R016 — Check "Existing structure sections TITLE" like height, model
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 2
- **Reference image:** 2-Existing structure sections TITLE.png
- **Evidence:** Drawing shows 'EXISTING INDARA ROOFTOP SITE' but reference RFSNA table indicates structure owner should be 'Optus' (highlighted in yellow). The drawing title does not specify the structure type, height, or model number. Reference shows structure should be identified with these complete details.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R028 — If Electrical upgrade is required, please add E1 & E2 sheets. For E3 sheets add the standard notes in G3 sheets.
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 2
- **Reference image:** 12-Electrical Installation and site earthing.png
- **Evidence:** The drawing indicates that electrical upgrade is required ('EXISTING 50A 3PH AC POWER SUPPLY IS NOT SUFFICIENT FOR THE PROPOSED UPGRADE PROJECT AND REQUIRES TO BE UPGRADED TO G3A 3-PHASE REFER TO DRGS. M8798-E1 AND E2 FOR ELECTRICAL SPECIFICATIONS'). However, no E1, E2, or E3 sheets are visible in the provided FC drawing pages. The reference to these sheets exists but the actual sheets are not included in the submission.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R034 — Notes & Legend details included
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 3
- **Reference image:** 5-Standard note-legend.png
- **Evidence:** The drawing includes a NOTES section with standard notes (items 1-5) and a LEGEND section. However, the legend is incomplete compared to the reference image. The drawing legend shows only 3 items (EXISTING PROPERTY BOUNDARY, EXISTING LEASE AREA, EXISTING OPTUS U/G POWER SUPPLY) but is missing legend entries for other line types visible in the drawing such as EXISTING O/H POWER SUPPLY (yellow line), EXISTING U/G POWER SUPPLY (orange line), EXISTING FENCE LINE (orange dashed), and PROPERTY BOUNDARY (magenta line) that are shown in the reference image. The legend does not comprehensively show all line types and symbols actually used in the drawing.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R036 — Scale shown and correct ( Eg. 1:100) & New equipment shown as BOLD
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 4
- **Reference image:** 3-SCALE & Viewport.png
- **Evidence:** Scale shown as 1:200 in the detail callout box on the drawing, but the viewport properties show Standard scale as 1:100_1 and Annotation scale as 1:100. There is a mismatch between the scale displayed on the drawing (1:200) and the viewport scale settings (1:100). Additionally, no new equipment is visibly shown in BOLD formatting on this drawing page.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R039 — Show shelter callout
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 4
- **Reference image:** 6-Shelter callout.png
- **Evidence:** No shelter callout is visible on the FC drawing page provided. The reference image shows a clear shelter callout that states 'OPTUS EQUIPMENT SHELTER SUPPORTED ON STRIP FOOTINGS AND PIERS. REFER TO DRG H897-S1 FOR FOOTING DETAILS' with bold formatting and proper referencing. The FC drawing page does not contain any such shelter callout or reference to shelter specifications in bold layer.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R046 — Safety handrailing / anchor points shown  (Rooftop sites only)
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 4
- **Reference image:** 13-Safety handrail & Anchor point.png
- **Evidence:** The FC drawing page shows 'EXISTING OPTUS HANDRAIL' and 'EXISTING OPTUS HANDRAIL AROUND 3 SIDES OF WALKWAY' labeled on the plan, but these markings do not clearly correspond to or match the specific handrail and anchor point locations visible in the as-built reference photo. The reference photo clearly shows a hand rail with specific anchor points on the rooftop edge, and while the drawing mentions existing handrails, the drawing does not adequately show the detailed handrailing and anchor points as depicted in the photographic evidence (which is stated as final reference). The drawing lacks clear visual representation of the exact handrail configuration and anchor point details visible in the photos.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R049 — Access must be checked for antennas/RRUs. If any access restriction identified, please highlight to DE & CE at early stage.  (Refer snip 7 in next sheet for access details)
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** 17-ladder climbing clearance.png
- **Evidence:** The reference image explicitly highlights that 'the RRU is located within the climbing area, which causes an obstruction, so it should be moved to the other side as much as possible.' The FC drawing pages provided do not show any similar access obstruction analysis or highlights for antennas/RRUs. The drawing pages lack the required assessment of whether step-pegs or ladders on the tower/structure would have obstructions in their climbing areas, and there is no evidence that access restrictions have been identified and highlighted to DE & CE at the early stage as required by R049.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R059 — Does the headframe, antennas, shelter/ODU and other equipment need painting?
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 7
- **Reference image:** 10-paint & no paint.png
- **Evidence:** Reference image (left photo) clearly shows existing antenna mounting pole and equipment ARE painted green. The FC drawing notes section does not include any painting requirements or notes specifying that proposed equipment must be painted to match the existing green colour of the site infrastructure. The drawing notes (1-4) address antenna configurations, structural assessment, ancillaries, and corroded mounts, but do NOT include painting specifications despite the site requiring it per R059.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R060 — Show GPS, shelter & Existing callouts like fence, existing tower callout, other operator shelter callout.
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 7
- **Reference image:** 11-proposed GPS & shelter and existing callout.png
- **Evidence:** The FC drawing page shown does not display the required callouts for GPS, shelter, fence, existing tower, and other operator shelter callout in the same manner as shown in the G3 reference sheet. The reference image shows multiple specific callouts (EXISTING OPTUS 2.4m HIGH CHAINWIRE SECURITY FENCE, EXISTING TREES, EXISTING TELSTRA EQUIPMENT SHELTER, EXISTING SITE GROUP METER BOX, etc.) with clear annotation boxes. The FC drawing page provided shows a NORTHERN ELEVATION and SITE ELEVATION view but lacks the detailed existing condition callouts (GPS antenna callouts, shelter details, fence callout, existing tower information, other operator shelter callout) that match the G3 sheet reference callout style and content.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R067 — Show all equipment inside the shelter like existing damper, O/H cable tray & fan. Check all internal photos & update the floor plan
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 3-Existing internal shelter equipment location.png
- **Evidence:** The FC drawing layout plan shows equipment locations but does not include internal photographs or visual confirmation of all internal equipment placement. While the drawing shows equipment positions (NEW VODAFONE VERTIV PSU-2, NEW OPTUS VERTIV PSU-1, NEW ELTEK 3RU MER HFDC RACK, etc.), there is no evidence that internal shelter photos have been checked and cross-referenced to verify all equipment is correctly positioned. Critical items visible in the reference internal photos (ceiling fan, damper, cable tray routing, O/H cable connections) are not explicitly detailed or verified against actual internal conditions in the provided drawing documentation. The drawing references notes but does not demonstrate photographic verification of equipment placement as required by the rule.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R076 — Remove Huawei PSU/Invenys and any batteries older than 5 years after the new installation
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 11-Huawei PSU.png
- **Evidence:** Huawei PSU identified in reference image at top left with red box label 'HUAWEI PSU'. Drawing notes reference 'RECOVER EXISTING ELTEK 18kw PSU RACK RECTIFIERS' and 'NEW VERTIV 25kw DC POWER SYSTEM' but also references 'VODAFONE PSU-2: RECOVER EXISTING ELTEK 18kw PSU RACK RECTIFIERS AND BATTERIES' and multiple Huawei components visible in reference photo including Huawei power modules in lower section. The drawing does not clearly document removal of the Huawei PSU/equipment shown in the reference image before new installation.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R086 — Spell check done properly
- **Verdict:** FAIL
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** Duplicate notes1.png
- **Evidence:** Multiple spelling errors found: (1) 'INDARA' should be 'INDARA' - appears correct on review; (2) Reference document list shows 'OSD-TTI-2' and 'OSD-TTI-3' but content references 'SITE SIGNAGE LEGEND AND NOTES' - consistent naming; (3) In EXISTING INDARA ROOFTOP SITE section: 'ALLELECS' appears to be a truncation/error - should likely be 'ALLELECS' or similar; (4) EME EXCLUSION ZONES section references 'G3A 3-PHASE' formatting is unclear; (5) Duplicate callout check: No obvious duplicate callouts detected across pages. Primary concern: Spelling integrity in technical abbreviations and proper nouns requires verification against Optus standards.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R005 — Site number/Name/Address details correct
- **Verdict:** FAIL
- **Drawing:** input.pdf
- **Last seen:** 2026-03-24 12:53
- **Pages checked:** 0, 1, 2
- **Reference image:** 1-Site name-number-address.png
- **Evidence:** Site ID mismatch: Drawing shows H8099 but reference shows H8097. Site Name matches (AUSTINS FERRY). Address matches (LOT 13 PLAN 178737, POIMENA RESERVE, WAKEHURST RD, AUSTINS FERRY, TAS 7011). JV Site ID matches (JH3038).
- **Times seen:** 4
- **Confidence:** 0.554 🔴 Low

---


## TEXT001 — All text uppercase
- **Verdict:** FAIL
- **Drawing:** input.pdf
- **Last seen:** 2026-03-24 14:32
- **Pages checked:** N/A
- **Reference image:** N/A
- **Evidence:** Basic uppercase check
- **Times seen:** 5
- **Confidence:** 0.564 🔴 Low

---

