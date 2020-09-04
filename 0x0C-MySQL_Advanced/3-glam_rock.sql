-- advanced SQL task
-- sort by lifespan
SELECT band_name, ifnull(split, 2020) - ifnull(formed, 0) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
