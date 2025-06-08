from fastcore.all import *
from fastcore.py2pyi import create_pyi
from faststripe.core import StripeApi

import os

def main():
    config_path = Config.find("settings.ini").config_path
    # Generate base pyi
    create_pyi(config_path / 'faststripe/core.py')
    
    # Get existing content
    pyi_path = config_path / 'faststripe/core.pyi'
    base_content = pyi_path.read_text()
    
    # Extract resource groups from API instance
    sapi = StripeApi(os.getenv('STRIPE_SECRET_KEY'))
    resources = {k: v for k, v in sapi.__dict__.items() 
                 if hasattr(v, '__dict__') and not k.startswith('_')}
    
    # Generate type annotations
    attrs = [f'    {k}: {k.title()}' for k in resources]
    
    base_cls = '''
class _StripeResourceGroup:
    """Base class for Stripe resource groups with dynamic methods"""
    def create(self, **kwargs): ...
    def fetch(self, **kwargs): ...
    def delete(self, **kwargs): ...
    def update(self, **kwargs): ...
'''
    
    classes = []
    for k, v in resources.items():
        methods = []
        for n, m in v.items():
            methods.append(f'\tdef {n}{m.__signature__}:\n\t\t"""{m.__doc__}"""\n\t\t...')
        
        cls_def = f'''
class {k.title()}(_StripeResourceGroup):
{'\n'.join(methods)}
'''
        classes.append(cls_def)
    
    # Write complete pyi file
    full_content = base_content + '\n'.join(attrs) + '\n' + base_cls + '\n'.join(classes)
    pyi_path.write_text(full_content)

if __name__ == '__main__': main()