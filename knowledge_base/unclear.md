# UNCLEAR Knowledge Base

All rules that have returned UNCLEAR verdict.
Auto-updated after every validation run.

---

## R001 — Drawings must be correct scale in all the sheets
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 11:03
- **Pages checked:** 0, 1, 2
- **Reference image:** 1-SCALE & Viewport.png
- **Evidence:** The three FC drawing pages provided (M8398-00 cover sheet, M8398-01 reference documents sheet, and M8398-G1 site specifications sheet) are administrative/specification sheets that do not contain scaled technical drawings requiring a standard viewport scale. No plan, elevation, or detail drawings with scale notations are visible in the submitted pages to compare against the reference standard of 1:100. Additional drawing sheets (e.g., site plans, structural details, antenna details) would need to be reviewed to fully verify scale compliance across all sheets.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R002 — Check scale with viewport
- **Verdict:** UNCLEAR
- **Drawing:** input.pdf
- **Last seen:** 2026-03-24 12:53
- **Pages checked:** 0, 1, 2
- **Reference image:** 1-SCALE & Viewport.png
- **Evidence:** The FC drawing pages provided are static images without access to CAD software or viewport properties. The reference image shows a viewport dialog with 'Annotation scale: 1:100' and 'Standard scale: 1:100_1' visible. Page H8099-G2 shows 'SCALE 1:2000' for the Overall Site Plan, but without CAD access to verify the actual viewport scale settings and confirm they match, this cannot be definitively verified. The static drawing images do not provide visibility into the viewport scale configuration that CAD access would reveal.
- **Times seen:** 9
- **Confidence:** 0.591 🔴 Low

---


## R004 — Layers correcly followed
- **Verdict:** UNCLEAR
- **Drawing:** input.pdf
- **Last seen:** 2026-03-24 12:53
- **Pages checked:** 0, 1, 2
- **Reference image:** 3-Optus FC template Layer format.png
- **Evidence:** The FC drawing pages provided (H8099-00, H8099-G1, H8099-G2) are predominantly text, specifications, and site plans with minimal layer-dependent graphical elements visible. The overall site plan (H8099-G2) shows existing and proposed elements but the image resolution and contrast make it impossible to definitively verify whether existing elements use unbold/light layers versus proposed elements using bold layers. The legend on H8099-G2 indicates 'EXISTING' and 'PROPOSED' distinctions but layer weight/boldness cannot be clearly assessed from these images. A detailed layer inspection in the source CAD file would be required for accurate verification.
- **Times seen:** 9
- **Confidence:** 0.591 🔴 Low

---


## R005 — Site number/Name/Address details correct
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 1-Site name-number-address.png
- **Evidence:** FC drawing consistently shows Site M8398, DOREEN TOWNSHIP-O, 95 HAZEL GLEN DRIVE, DOREEN VIC 3754, RFNSA No: 3754005 across all pages. Cannot independently verify against RFSNA system — cross-check with RFSNA is required to confirm site number, name, and address details are correct as per the rule requirement.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R036 — Scale shown and correct ( Eg. 1:100) & New equipment shown as BOLD
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 3-SCALE & Viewport.png
- **Evidence:** The FC drawing pages provided (M8398-00, M8398-01, M8398-G1) are cover, index, and site specification sheets. M8398-G1 shows only a graphical scale bar but no standard ratio scale (1:100 format) is visible. No detailed plan/elevation viewport pages with equipment are included in the submitted pages to verify scale matching against viewport properties or bold formatting of new equipment. Cannot fully assess compliance without the detailed drawing sheets (G2, G3, etc.).
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R037 — Compound shown and referenced (as per Indara document for Indara site)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 4
- **Reference image:** 4-Compound dimension & lease.png
- **Evidence:** The FC drawing page shows a site layout plan but does not display clear compound area dimensions or lease area boundaries with specific measurements. The reference image shows detailed dimensional annotations (yellow highlighted areas with measurements), while the FC drawing lacks comparable dimensional details for the compound/lease area. Without access to the Indara document or previous As-Built drawings to compare against, and given the absence of clear dimensional references on the FC drawing itself, verification against those documents cannot be confirmed. The drawing shows 'EXISTING PROPERTY BOUNDARY' and 'EXISTING LEASE AREA' in the legend, but specific dimensions are not legible or clearly marked on this plan.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R038 — If site owner is INDARA & rooftop site, Earthing notes must be added in G3 sheet.
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 4
- **Reference image:** 5-Earthing appicable for rooftop.png
- **Evidence:** Drawing shows site layout M8398-G3 for a rooftop site (DOREEN TOWNSHIP-O). However, the site owner information (INDARA or otherwise) is not clearly visible or legible in the provided drawing page. The reference image discusses earthing specifications and OSD-020 OPTUS EARTHING SPECIFICATION requirements, but without confirmed site owner as INDARA, the applicability of R038 cannot be definitively determined. No specific earthing notes are visible in the G3 sheet provided.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R040 — GPS antenna shown: For Nokia region AYGE & Ericsson region GNSS GPS.
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 7-GPS callout.png
- **Evidence:** The FC drawing pages provided (M8398-00 title page, M8398-01 reference documents, M8398-G1 site specifications) do not contain the RRU schedule or GPS antenna model callouts needed to verify whether the correct GPS antenna (Nokia AYGE for Nokia RRUs or Ericsson GNSS GPS for Ericsson RRUs) is specified. The antenna system configuration sheets (M8398-A1, M8398-A2) and physical asset summary table (M8398-A3) required for this check were not included in the submitted pages.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R041 — Show removed feeders details & proposed Hybrid cables details. Please check proposed feeders can be possible to accommodate existing cable tray/ladder/underground conduit or internal monopole.
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 4
- **Reference image:** 8-Cable ladder callout.png
- **Evidence:** The FC drawing page provided shows a Site Layout and Setout Plan with antenna positioning and general site infrastructure details. However, the specific details required by R041 are not clearly visible on this page: (1) Removed feeders details are not explicitly documented in a dedicated section, (2) Proposed Hybrid cables details are not shown with specifications, (3) Cable tray/ladder/underground conduit accommodation verification is not evident, (4) Internal monopole routing is not addressed. The reference image shows detailed feeder notes and hybrid cable specifications in red text on the right side, but these detailed feeder scope items and phase 1 RLM & FR cross-references are not present on the submitted drawing page. Additional drawing pages may be required to fully verify this rule.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R042 — G3 sheet - Antenna tagged shown
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 4
- **Reference image:** 9-Antenna tag label.png
- **Evidence:** The FC drawing page shown is a site layout and setout plan at 1:200 scale showing overall site configuration. While antenna legend is present and some antenna tags are visible on the drawing (marked with antenna symbols), the resolution and scale of this overview drawing make it difficult to clearly verify that all antenna tags including antenna numbers and azimuths are shown correctly and match with RLM & FR specifications. The drawing appears to be a general layout plan rather than a detailed G3 antenna tag verification sheet. A higher resolution detailed antenna elevation/section view would be needed to properly verify antenna tag accuracy, azimuth orientation, and proper tag placement relative to antenna blocks for multiple antennas at the same pole.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R043 — Update EME comments as per OSD-171 document & Form A/B.
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 4
- **Reference image:** 10-Site signage G3 sheet.png
- **Evidence:** The FC drawing page shows multiple signage-related items in the text callouts (e.g., 'EXISTING FADED HAZARDOUS VOLTAGE SIGN ON METER BOX TO BE REPLACED WITH NEW SIGNAGE', 'REMOVE EXISTING MERCS#1 SIGNAGE FROM SHELTER', 'REMOVE EXISTING MERCS#2 SIGNAGE FROM SHELTER ACCESS DOOR'). However, without access to the Form A/B documentation, OSD-171 document, or SDV photos referenced in the rule, I cannot verify whether the site signage shown matches the required specifications or whether the leader lines point to the correct positions as per those reference documents. The reference image indicates these items should be checked but the actual validation documents are not provided.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R044 — Roof levels shown (Rooftop sites only)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 11-Roof level in G3 sheet.png
- **Evidence:** The FC drawing pages provided (M8398-00, M8398-01, M8398-G1) do not show roof level elevations. The Site Specifications sheet (M8398-G1) mentions '8.65m HIGH BUILDING PARAPET WALL' but does not show labeled roof level elevations (RL/AHD values) as required and shown in the reference image. The Site Elevation sheet (M8398-G4) is listed in the drawing register but was not included in the provided pages for review — roof levels may be present on that sheet.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R046 — Safety handrailing / anchor points shown  (Rooftop sites only)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 13-Safety handrail & Anchor point.png
- **Evidence:** The FC drawing pages provided only include the cover sheet (M8398-00), reference documents (M8398-01), and site specifications (M8398-G1). No site layout/plan drawings (e.g., G2/G3) are included in the submitted pages to verify if handrailing and anchor points are graphically shown as required. The site specs note mentions a fall arrest system but no handrail or anchor point callouts are visible in the drawings provided for review.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R047 — Panel/AAU antenna(s) shown, orientation
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 4
- **Reference image:** 14-antenna dimension.png
- **Evidence:** The FC drawing page shown is a site layout and setout plan at 1:200 scale. While antenna legend symbols are present, the specific antenna model (RRV2VV-6533D-R8 with dimensions 2577 x 498 x 197) and azimuth orientations are not clearly visible or callout-annotated on this overview drawing page. The reference image shows detailed antenna specifications with model and dimensions highlighted, but these details are not legible or present on the provided FC drawing page. To fully verify R047 compliance, a more detailed antenna installation drawing or closer view showing antenna azimuth angles and model callouts would be required.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R048 — Maintain 500mm Horizontal, Maintain 70° for passive antennas & 60° AAUs Angular separation. If this separation is not achieved, please highlight to DEs & TL
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** 15-Horizontal separation.png
- **Evidence:** The provided FC drawing pages (M8398-00, M8398-01, and M8398-G1) are cover/specification pages that do not contain detailed antenna layout drawings with measurements. The reference image shows antenna separation measurements (843.49 mm horizontal distance and angular separations of 190°, 180°, 210°), but the actual FC drawing pages provided do not show the antenna configuration details needed to verify the 500mm minimum horizontal separation and 70°/60° angular separation requirements. Detailed antenna layout/configuration drawings (such as M8398-A1 or M8398-A2 referenced in the drawing index) would be required to properly assess compliance with R048.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R049 — Access must be checked for antennas/RRUs. If any access restriction identified, please highlight to DE & CE at early stage.  (Refer snip 7 in next sheet for access details)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 17-ladder climbing clearance.png
- **Evidence:** The site specifications (M8398-G1) confirm that ladder and step pegs with fall arrest system are present on the rooftop and mounting pole, meaning climbing area clearance must be checked per the rule. However, the antenna layout plan, elevation drawings, and RRU/antenna mount detail sheets (M8398-G4, S4-S8) were not provided in the FC drawing pages, so it cannot be confirmed whether any RRU or antenna obstructs the climbing area. A full check requires review of the antenna layout plan and elevation drawings to verify no obstructions exist in the climbing path.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R050 — Antenna, RRU, Combiner/Filter model & QTY need to matches FR/RLM/DPD
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** 18-Antenna, RRU & Combiner callout.png
- **Evidence:** The FC drawing pages provided (M8398-00, M8398-01, and M8398-G1) are cover sheets, reference documents page, and site specifications page. They do not contain detailed antenna, RRU, combiner/filter model numbers and quantities in a format that can be compared against RLM, DPD, or FR documents. The reference image shows these details should appear on antenna system configuration sheets and site layout/setout plans, but the specific sheets containing antenna callouts, model numbers, and quantities are not included in the provided FC drawing pages. To properly verify R050, sheets such as 'eJV ANTENNA SYSTEM CONFIGURATION' or detailed antenna layout sheets with specific model callouts and quantities need to be reviewed.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R051 — Antenna numbering conforms to OSD70 and RF guidelines - Sector arrow shown correctly for new antenna and existing antennas with ("J" for joint venture and "O" for optus)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** 19-Antenna tag number.png
- **Evidence:** The FC drawing pages provided show site specifications and general information but do not contain antenna layout diagrams or antenna numbering details. The reference image shows antenna numbering format (11-J, 22-J) with sector arrows and J/O/V designations, but the actual antenna configuration drawings (M8398-A1 and M8398-A2 mentioned in the drawing index) are not visible in the provided pages. Cannot verify antenna numbering compliance without seeing the actual antenna configuration sheets.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R052 — New structural design layout (Face mount, headframe from 3rd party or structural H frame, etc) incorporated in this drawing?
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** 20-mount design layout.png
- **Evidence:** The FC drawing pages provided (M8398-00, M8398-01, and M8398-G1) are cover sheets, reference documents, and site specifications pages. They do not contain the detailed antenna layout plans, structural drawings, or mount details needed to verify R052. The reference image shows an antenna layout plan with structural design details and callouts, but the actual antenna system configuration sheets (M8398-A1 and M8398-A2 referenced in the drawing index) are not included in the pages provided for review. Cannot determine if proposed antennas use existing or new mounts, or verify structural design callouts without the detailed antenna configuration and structural detail sheets.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R053 — Legends and notes shown and read correctly
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 21-Notes - paint.png
- **Evidence:** The Antenna Layout Plan sheets (M8398-A1 to A3) which should contain the standard notes (antenna orientations, DRG references, corroded U-bolts) and antenna legend are not included in the FC drawing pages provided for review. Only the title sheet (M8398-00), reference documents sheet (M8398-01), and site specifications sheet (M8398-G1) were provided. Cannot verify whether standard notes, site-specific painting notes, and antenna legend are correctly shown on the antenna layout plan sheets.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R054 — Overall structural height EL noted and RL shown at ground level datum point
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 7
- **Reference image:** 1-Top of tower height.png
- **Evidence:** The FC drawing page shown is a Northern Elevation and Site Elevation plan view with multiple antenna mounting details and structural notes. However, the overall structural height EL (Existing Level) and RL (Reduced Level) at ground level datum point are not clearly visible or legible in the provided FC drawing page. The reference image shows EL 23.25m marked at the top with 'OVERALL HEIGHT' annotation and ground datum RL clearly marked, but the FC drawing page does not display these critical measurements with sufficient clarity to verify compliance with R054. Additional drawing pages or a clearer view of the elevation section with explicit EL and RL markings at the top and ground datum would be needed to confirm PASS or FAIL.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R055 — Antenna model name, QTY & Elevation level
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 7
- **Reference image:** 3-Antenna model & ACL - Cert.png
- **Evidence:** The FC drawing page shows a Northern Elevation view with multiple antenna installations listed in the left annotation block (EL 57.95m, EL 12.20m, EL 9.55m, EL 8.35m, EL 8.37m, EL 0.50m). However, the drawing does not provide a clear antenna schedule table showing antenna model names, quantities, elevation levels, and ACL measurements in a format that can be comprehensively cross-referenced against DPD/FR/RLM/RFSNA/Structural certifications. The reference image shows a detailed table with Height AGL, Qty, Antenna/Equipment type, Azimuth, and Status columns which is not visible in this FC drawing page. Without access to the complete antenna schedule table and certification documents, verification of antenna model matching, ACL alignment, and minimum 300mm separation between multiple AAUs cannot be definitively confirmed.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R056 — RRU model, QTY & Elevation level
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 7
- **Reference image:** 5-RRU model & ACL - Cert.png
- **Evidence:** The FC drawing page shows a Northern Elevation and Site Elevation view but does not provide a clear Loading Arrangement table or RRU specification details visible in this page. The reference image shows a Loading Arrangement table with RRU models (RRU4440, RRU4466, Future RRU, AHFA, AHLGA, REJ FILTER) at heights 23.1m with quantities and azimuth details. The current FC drawing page lacks the detailed RRU model, QTY, elevation level information, and separation distance verification that would be needed to fully validate R056. Without access to the DPD/Structural certificate or complete RRU specifications on this drawing page, cannot definitively verify: (1) RRU level alignment between FC and Structural cert, (2) RRU model compliance with DPD/Structural cert, or (3) minimum 300mm separation between RRUs.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R057 — Feeders model & Qty and feeders route details
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 7
- **Reference image:** 7-cable route details.png
- **Evidence:** The FC drawing shows feeder cable routing details with reference to existing OPTUS 450mm wide cable tray at ground level and installation of new H&S 6/12 hybrid cables in existing OPTUS 450mm wide cable ladder. However, the drawing does not provide sufficient detail to verify: (1) complete feeder model & quantity specifications against Phase 1 RLM and FR documents, (2) comparison of cable routing methodology (horizontal cable tray/underground conduit vs. vertical cable ladder/monopole strapping) between G2 sheet and elevation views, and (3) confirmation that existing cable route capacity is adequate for proposed feeder scope. The drawing references existing cable infrastructure but lacks explicit verification statements and comparative analysis required by R057.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R058 — Panel/Parabolic antenna heights noted (CL). Vertical clearance dimensions between new and existing antennas mentioned
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 9-other operator antennas.png
- **Evidence:** The FC drawing pages provided (M8398-00 cover sheet, M8398-01 reference documents, and M8398-G1 site specifications) do not include the Site Elevation drawing (M8398-G4) where antenna centerline heights (CL) and vertical clearance dimensions between new and existing antennas would typically be shown. The reference image demonstrates the correct format with EL heights noted for each antenna level and vertical separations shown. Without the elevation drawing page being provided, it is not possible to verify compliance with this rule.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R059 — Does the headframe, antennas, shelter/ODU and other equipment need painting?
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 10-paint & no paint.png
- **Evidence:** The FC drawing pages do not include site photos showing whether existing antennas, mounts, or steelwork are painted. No painting notes are present in the drawing's Notes section. The Equipment Shelter is noted as coloured 'white', but there is no explicit statement or note addressing whether proposed equipment needs to be painted to match existing. Per the rule, site photos should be checked and painting notes added to 'Notes' if required — neither is visible in the provided pages.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R060 — Show GPS, shelter & Existing callouts like fence, existing tower callout, other operator shelter callout.
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 11-proposed GPS & shelter and existing callout.png
- **Evidence:** The FC drawing pages provided (M8398-00, M8398-01, M8398-G1) do not include the Site Elevation sheet (M8398-G4) or G3 sheet where GPS, shelter, fence, existing tower, and other operator shelter callouts should appear. The relevant elevation drawing required to verify this rule was not supplied for review.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R061 — ROOFTOP SITE - Separation Distance between base of antenna and rooftop provided?
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 12-Base separation & 5m rule.png
- **Evidence:** The FC drawing pages provided (cover sheet M8398-00, reference documents M8398-01, and site specifications M8398-G1) do not include the antenna mount detail or section drawings where the separation distance between the antenna base and rooftop would be shown. The structural antenna mount detail sheets (M8398-S4 through S7) referenced in the drawing register were not provided for review. Cannot confirm presence of minimum 400mm separation dimension without these sheets.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R063 — Check DPD legends are standard or not
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** DPD legend.png
- **Evidence:** The FC drawing pages provided (M8398-00, M8398-01, M8398-G1) are the cover sheet, reference documents, and site specifications pages. None of these pages contain a DPD legend. The DPD legend would typically appear on the RF plumbing diagram or antenna system configuration sheets (e.g., M8398-P1, M8398-A1/A2), which were not included in the submitted pages. Unable to verify compliance with the latest DPD legend standard without the relevant drawing pages.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R064 — Conjuction notes to refer A1 sheet
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** DPD notes.png
- **Evidence:** The FC drawing pages provided (M8398-00, M8398-01, M8398-G1) do not include the RF Plumbing/A1 sheet where the conjunction note 'THIS DRAWING SHALL BE READ IN CONJUNCTION WITH DRAWING [SiteID]-A1, A2 & A3' would typically appear. The A1 sheet (M8398-A1) is listed in the drawing index but not provided for review, making it impossible to verify the conjunction note Site ID and drawing number reference.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R065 — Shelter type with door swing direction correct
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 1-Door opening.png
- **Evidence:** The FC drawing page shows an Equipment Shelter Layout Plan with detailed interior rack configurations, but does not clearly show the shelter door or its swing direction. The reference image shows a door with a specific swing direction (opening outward/rightward based on the red arrow annotation), but the drawing page provided does not contain a clear elevation view or floor plan perspective that definitively shows the door swing direction for verification against the reference photo.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R066 — Internal rack number to be anticlockwise as enter the shelter,  number G000 for ground & R000 for rooftop
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 2-Rack number.png
- **Evidence:** The drawing shows rack numbers (F01, F02, F03, F04, F05 in upper level and IF01, IF02, IF03, IF04, IF05 in lower level) but the prefix 'F' does not match the required standard of 'G000' for ground-based sites or 'R000' for rooftop sites. The anticlockwise direction assignment cannot be definitively verified from this layout plan alone, and the site type (ground vs rooftop) is not explicitly stated on this page. Additional clarification needed on whether this is a ground or rooftop site and whether the 'F' prefix is acceptable or should be 'G' or 'R'.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R067 — Show all equipment inside the shelter like existing damper, O/H cable tray & fan. Check all internal photos & update the floor plan
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 3-Existing internal shelter equipment location.png
- **Evidence:** The Equipment Shelter Layout Plan drawing (M8398-F1) was not included in the FC drawing pages provided for review. Only the cover sheet (M8398-00), reference document sheet (M8398-01), and site specifications (M8398-G1) were provided. Without the actual floor plan page, it is impossible to verify whether the existing damper, O/H cable tray, and fan are correctly shown in the correct locations as required by the rule.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R068 — Glandplate sufficient for upgrade works
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 4-Gland window.png
- **Evidence:** The equipment shelter layout plan shows gland plate details and existing cable routing, but no actual gland window photograph is provided in the FC drawing pages to visually confirm available space for proposed additional feeders. The drawing references 'EXISTING GLAND PLATE (660x420)' in the shelter details section, but without a photo of the actual gland window showing current occupancy and remaining capacity, it is not possible to definitively verify whether sufficient space exists for the upgrade works proposed in the drawing.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R069 — Existing A/C units quantity mentioned including existing stacker frame
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 5-AC units callout.png
- **Evidence:** The FC drawing pages provided are cover sheets and site specifications (M8398-00, M8398-01, M8398-G1) and do not include the equipment shelter layout plan (M8398-F1) where the existing AC unit quantity and stacker frame callout would be shown. The reference image indicates the correct callout should read 'EXISTING 3 STACKER CAGE + L600P AIR CONDITIONERS (2 OFF)' based on site photos. Cannot verify compliance without the F1 shelter layout drawing page.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R071 — Remove Huawei BTS rack
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 7-RFM & BBU.png
- **Evidence:** The FC drawing shows recovery of EXISTING Huawei BTS racks (1 OFF) in multiple locations (LEFT, MIDDLE positions) as noted in the shelter details section. However, the drawing does not clearly specify QTY of Huawei BTS racks to be REMOVED in the proposed scope, nor does it explicitly confirm removal of OLD type RFM and BBU units associated with the Huawei BTS rack removal. The reference photo shows RFM and BBU components, but the drawing lacks detailed callouts confirming these OLD type components are included in the removal scope.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R072 — Please make sure use proper BTS equipment based Nokia BBU or Ericsson BBU
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 8-BBU, power up BBU & Alarm.png
- **Evidence:** The drawing shows multiple RRU types being deployed (Ericsson 3RU MER BTS RACK and Vodafone L8/5 & LU7 HUAWEI BTS RACK visible), but the specific RRU models and their corresponding BBU models are not clearly legible in the provided FC drawing pages. The notes reference new Ericsson BBU's (5 OFF) and new Vodafone equipment deployment, but exact BBU model numbers (such as RP6651 or BBU6672 for Ericsson, or specific Nokia AirScale variants) cannot be definitively confirmed from the drawing resolution and text clarity provided. A higher resolution or clearer specification is needed to verify proper BBU-to-RRU matching.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R073 — Existing Krone panel to be upgraded
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 9-Krone-RJ45 Alaram panel.png
- **Evidence:** The FC drawing pages provided (M8398-00, M8398-01, M8398-G1) are cover sheet, reference documents, and site specifications pages only. The Equipment Shelter Layout Plan (M8398-F1) where alarm panel details would be shown is not included in the provided pages. No mention of Krone panel upgrade to RJ45 or 6610 PSU alarm panel is found in the visible pages, making it impossible to verify compliance with the Krone-to-RJ45 upgrade rule.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R074 — Existing Skinny MER rack & 15-way iDCDP reused - please make sure more than 15-iDCDP are not accommodate.
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 15 Way IDCDP.png
- **Evidence:** The drawing shows references to 'RECOVER EXISTING iDCDP (1 OFF) ALL CORDONING AS WELL' and mentions of existing racks, but the specific iDCDP type (whether it is 15-way or another configuration) cannot be clearly determined from the drawing pages provided. The drawing references existing MER racks and iDCDP recovery, but does not explicitly state the iDCDP capacity rating. Without clear visual confirmation or explicit labeling of the iDCDP type in the provided images, it cannot be definitively verified whether the existing iDCDP is exactly 15-way and whether proposed equipment accommodations comply with the 15-way limitation for existing skinny MER racks.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R075 — Existing/New 18-way/22-way iDCDP proposed for new/existing 37RU MER rack
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 22-way iDCDP.png
- **Evidence:** The FC drawing page shown is an Equipment Shelter Layout Plan that does not contain detailed iDCDP specifications or capacity information. The drawing shows general equipment layout including references to 'iDCDPs/DCDUs AND MER RACK' but does not explicitly state the existing iDCDP capacity (22-way vs 18-way) or confirm whether the existing 22-way iDCDP is sufficient for the proposed upgrade works. Additional detailed equipment specifications or MER rack documentation would be needed to verify this rule.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R076 — Remove Huawei PSU/Invenys and any batteries older than 5 years after the new installation
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 11-Huawei PSU.png
- **Evidence:** The FC drawing pages provided (cover sheet, reference documents, and site specifications) do not include the electrical specifications (M8398-E1), single line diagram (M8398-E2), or equipment shelter layout plan (M8398-F1) which would contain PSU type details and battery information. No mention of Huawei PSU/Invensys removal or battery age requirements was found in the available pages. The relevant electrical drawings are referenced but not provided for review.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R077 — Propose or reuse existing PSU & rectifier based on PDT. For eJV min 18KW are required whereas Optus only site use Min. 16kW PSU. If less than this condition, replace with new one.
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 12-PSU model & rectifier.png
- **Evidence:** Drawing shows PSU details but PDT (Project Design Template) information is not visible in the provided FC drawing pages. The drawing references 'NEW VERTIV 25kW DC POWER SYSTEM' and 'NEW OPTUS VERTIV PSU-1' and 'NEW OPTUS VERTIV PSU-2', indicating Vertiv PSUs are proposed. However, without access to the PDT showing site type (eJV vs Optus-only) and existing PSU capacity, cannot confirm if the 25kW capacity meets the minimum requirements (18kW for eJV, 16kW for Optus-only sites) or if replacement is justified.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R078 — Battery type & Model. If an Optus shelter is installed inside a Telstra exchange building, lithium batteries are not allowed. Even if the shelter is installed outside but within 2 m of the Telstra exchange room, lithium batteries are still not allowed
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-19 12:00
- **Pages checked:** 0, 1, 2
- **Reference image:** 12-PSU model & rectifier.png
- **Evidence:** The FC drawing pages do not include a PSU/PDT sheet showing the battery model and type (no PRP-SOL or equivalent sheet visible). The site is an Indara rooftop installation (not a Telstra exchange building), so lithium batteries would be permissible. However, the battery model cannot be confirmed from the provided FC drawing pages as the electrical/PDT summary sheet is missing. The shelter location is confirmed as rooftop (non-Telstra exchange), which satisfies the location condition of the rule.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R079 — Replace/reuse PSU CB size based on PDT tools - Vertiv PSU min. required 40A 1P CB (3 OFF)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 13-PSU CB size in PDT.png
- **Evidence:** The reference image shows PSU CB ratings being changed from 32A (existing) to 40A (proposed) for PSU 1 and PSU 2, which aligns with the rule requirement of minimum 40A 1P CB for Vertiv PSU. However, the FC drawing page provided is an Equipment Shelter Layout Plan that does not contain specific PSU CB details or PDT tool specifications. Cannot verify if this is the correct replacement based on PDT tools or confirm the 3 OFF configuration. The reference image shows only 2 PSUs being changed to 40A, not 3 OFF as stated in the rule.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R084 — All the existing and proposed equipments and texts layers are correct
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** Layer Bold-Unbold.png
- **Evidence:** The provided FC drawing pages (M8398-00, M8398-01, and M8398-G1) are cover/specification sheets and do not contain detailed equipment layout drawings with visible layer distinctions. While the reference image shows text callouts in unbold (existing) vs bold (proposed) layers on a technical drawing, the actual equipment layout drawings with layer information are not visible in the provided pages. Cannot verify if existing equipment/callouts are in unbold layers and proposed equipment/callouts are in bold layers throughout the project without access to the actual technical layout pages.
- **Times seen:** 2
- **Confidence:** 0.525 🔴 Low

---


## R018 — Structural adequecy of pole & foundation (Point 2)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 2
- **Reference image:** 4-Existing structure sections.png
- **Evidence:** The FC drawing page provided does not contain pole/tower and foundation structural adequacy certification information. The page shows site address, existing site hazards, site signage, EME exclusion zones, equipment shelter, transmission, and construction site access details. To verify R018, the drawing pages containing the structural adequacy certificate (such as Gamcorp Foundation Certificate 16721 dated 02-Sep-2025 by Lena Van Spaandonk) need to be reviewed. The reference image shows the certificate details are present in the design assessment document, but they are not visible in the FC drawing page provided for QA checking.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R019 — Check callout for Panel/RRU/AAU to be installed on existing or new mount (Point 3)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 2
- **Reference image:** 5-Existing structure sections (Structural drawing number).png
- **Evidence:** The drawing page shown is a site specifications and general information sheet. While it references 'NEW PANEL ANTENNAS TO BE INSTALLED ON EXISTING TURRET ON EXISTING MOUNTING POLE' and 'NEW RRUs TO BE INSTALLED ON EXISTING RRU MOUNT', there is no detailed plan view (G3-1) or structural drawing visible to verify whether new mounts are proposed and if their structural drawing numbers are properly callout. The structural drawing reference (M8398-1 mentioned for Equipment Shelter) is shown, but a complete plan view showing all Panel/RRU/AAU mount details and their callouts is not provided in the pages shown.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R020 — Structural adequecy of mount (Point 4)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 2
- **Reference image:** 6-Existing structure sections.png
- **Evidence:** The FC drawing page does not contain a structural adequacy certificate or mount certifier information. The reference image shows a 'Structural Analysis and Design Certificate' with reference number SC18415/OPTE, but this certificate is not visible on the provided FC drawing page. The drawing references 'EXISTING INDARA ROOFTOP SITE' and mentions antenna maintenance by qualified personnel, but lacks the specific mount certifier's name, date, and pass/fail status required by R020.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R024 — Site hazards updated as per site specific requirements. (Refer previous AB & SDV photos)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 2
- **Reference image:** 10-Site Hazard.png
- **Evidence:** The drawing lists 'EXISTING SITE HAZARDS' section with 9 numbered items (existing EME transmitting antennas & cabling, manual handling, working at heights, slip/trip/falls, electrical hazards, weather/lightning, wildlife/insects, unprotected roof edges, traffic management). However, the drawing does not include references to previous AB (As-built) & SDV photos, nor does it show evidence that site hazards have been updated based on those specific photo references. The hazard list appears to be generic/standard rather than site-specific as required by the rule.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R027 — Update Electrical Installation and site earthing as per CPS recent remarks. (Only CPS)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 2
- **Reference image:** 12-Electrical Installation and site earthing.png
- **Evidence:** The drawing states 'EXISTING 50A 3PH AC POWER SUPPLY IS NOT SUFFICIENT FOR THE PROPOSED UPGRADE' in the EME Exclusion Zones section. However, the drawing does not clearly indicate whether an electrical upgrade is required or not required. The reference to 'not sufficient' suggests upgrade may be needed, but there is no explicit statement. Standard notes about power supply based on PVA report are not visible on this page.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R029 — WHS design risk assessment note included for CPS only. (Not appliable for Servicestream)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 2
- **Reference image:** 13-WHS safety risk assessment.png
- **Evidence:** Drawing page shows site specifications and hazards list but does not contain explicit WHS design risk assessment notes. The 'EXISTING SITE HAZARDS' section lists 9 hazard categories but lacks detailed safety measures or risk assessment documentation. The contractor is mentioned as Servicestream, which according to the rule means WHS design risk assessment note may not be applicable. However, without clear indication of whether this is a CPS (Optus) or Servicestream project scope, and without visible WHS risk assessment documentation on the drawing, verdict cannot be definitively determined.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R030 — Update Corrosion Protection note on G1 page. (Only Servicestream site)
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 2
- **Reference image:** 14-Corrosion protection.png
- **Evidence:** The drawing page shown is a site specifications/general arrangement page (M8398-G1 A) that does not display the CORROSION PROTECTION section visible in the reference image. The corrosion protection note with corrosivity category and proposed protection system details is not present on this page. Cannot verify if the corrosion protection note has been updated per the rule requirements without viewing the actual corrosion protection details section of the G1 page.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R062 — Calculate RF tail length for all RRUs - please consider horizontal & vertical distance for tail calculation
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 8, 9
- **Reference image:** Tail length calculation 1.png
- **Evidence:** The FC drawing pages provided (A1 and A2) show antenna system configuration tables and details but do NOT include a Plan View G3-1 sheet. The reference image shows a plan view with RRU positioning and annotation indicating vertical distance of 6m exceeding the 4.7m threshold, requiring RF tail length calculation of 8.3m. Without access to the actual Plan View G3-1 sheet in the FC drawing pages to verify RRU-to-antenna distances and confirm whether RF tail length calculations have been properly documented, compliance with R062 cannot be determined. The antenna configuration sheets alone do not show RF tail length specifications or distance calculations.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R080 — Mention PDT approved version number. Please make sure use recent PDT tools
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 15-PDT version number.png
- **Evidence:** The reference image shows a dashboard with 'Ver 12.7' displayed in a blue box in the top right corner of the Site Details section. However, the FC drawing page provided does not show this dashboard or PDT version information. The drawing page shows an Equipment Shelter Layout Plan but does not display any PDT version number or reference to approved PDT tools. Cannot verify if the drawing matches the reference PDT version (12.7) or if it uses a recent approved PDT tool version without seeing the complete drawing documentation or RLM details.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R081 — Ensure the exact AC power supply value is mentioned, and it must align with the PVA, power meter photos, and SLD. Also, confirm if a power upgrade is required
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 19
- **Reference image:** 16-AC power supply.png
- **Evidence:** The drawing shows AC POWER SUMMARY with PDT indicating 'EXISTING OPTUS 50A THREE PHASE POWER SUPPLY IS SUFFICIENT FOR THE PROPOSED UPGRADE' and AC Mains Capacity showing Existing/Proposed/Supply all at 50A with 3P 415V. However, the PVA report table shows 'Existing 50A 3P confirmed' for Optus. The drawing lacks explicit reference to the PVA report document itself and does not clearly show comparison between existing power availability (50A) and proposed design load (31-40A normal/peak from PDT). While the yellow highlight states sufficiency, there is no documented cross-reference to PVA report, RLM values, or explicit power upgrade requirement assessment visible on this page.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

## R083 — All text font in ISOCP
- **Verdict:** UNCLEAR
- **Drawing:** M8398_DOREEN TOWNSHIP_FC_30052025 (2).pdf
- **Last seen:** 2026-03-23 10:35
- **Pages checked:** 0, 1, 2
- **Reference image:** Text style.png
- **Evidence:** The reference image shows text properties dialog with Style set to 'ISOCP', which is the correct font standard. However, in the FC drawing pages provided (M8398-00, M8398-01, and M8398-G1), I cannot directly access or inspect the text style properties of individual text elements to verify they are all in ISOCP font. The drawings display text content but do not show style property dialogs. A detailed examination of text properties would require opening each text element in the CAD software, which is not possible from static image review alone. Based on visual inspection, the text appears consistent and professional, but verification of ISOCP compliance cannot be definitively confirmed from these images.
- **Times seen:** 1
- **Confidence:** 0.5 🔴 Low

---

