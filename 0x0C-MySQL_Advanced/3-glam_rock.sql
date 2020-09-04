-- advanced SQL task
-- sort by longevity
SELECT band_name, ifnull(split, 2020) - ifnull(formed, 0) AS longevity FROM metal_bands WHERE style LIKE '%glam rock%' ORDER BY longevity DESC;
