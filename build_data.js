const fs = require('fs');
const path = require('path');

function buildData() {
    const examplesDir = path.join(__dirname, 'examples');
    const skills = [];

    if (!fs.existsSync(examplesDir)) {
        console.error(`Error: ${examplesDir} does not exist.`);
        return;
    }

    const entries = fs.readdirSync(examplesDir, { withFileTypes: true });
    for (const entry of entries) {
        if (!entry.isDirectory()) continue;
        
        const skillPath = path.join(examplesDir, entry.name, 'SKILL.md');
        if (fs.existsSync(skillPath)) {
            try {
                const content = fs.readFileSync(skillPath, 'utf-8');
                let name = entry.name;
                let description = '無提供描述。';
                let tags = [];
                
                const match = content.match(/^---\s*\n([\s\S]*?)\n---\s*\n/);
                if (match) {
                    const yamlPart = match[1];
                    const nameMatch = yamlPart.match(/^name:\s*(.*?)$/m);
                    if (nameMatch) name = nameMatch[1].trim();
                    
                    const descMatchMulti = yamlPart.match(/^description:\s*\|([\s\S]*?)(?:^[a-z]+:|\Z)/im);
                    if (descMatchMulti) {
                        description = descMatchMulti[1].trim();
                    } else {
                        const descMatch = yamlPart.match(/^description:\s*(.*?)$/m);
                        if (descMatch) description = descMatch[1].trim();
                    }
                    
                    const tagsMatch = yamlPart.match(/^tags:\s*\[(.*?)\]/m);
                    if (tagsMatch) {
                        tags = tagsMatch[1].split(',').map(t => t.trim()).filter(Boolean);
                    }
                }
                
                skills.push({
                    id: entry.name,
                    name,
                    description,
                    tags,
                    system_prompt: content
                });
                console.log(`Successfully loaded: ${name}`);
            } catch (err) {
                console.error(`Failed to read ${skillPath}:`, err);
            }
        }
    }

    const outputPath = path.join(__dirname, 'skills_data.js');
    try {
        fs.writeFileSync(outputPath, 'window.NUWA_SKILLS = ' + JSON.stringify(skills, null, 2) + ';\n', 'utf-8');
        console.log(`Generated ${outputPath} with ${skills.length} skills.`);
    } catch (err) {
        console.error('Failed to write JS data file:', err);
    }
}

buildData();
